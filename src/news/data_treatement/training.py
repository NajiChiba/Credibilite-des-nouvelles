import pandas as pd
import string
import re
import pymongo
import sklearn as sklearn
from mongoengine import connect
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle



#collect data (news-real & fake) from mongodb database
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


def getDataFromDb():
    try:
        # --- Connection to Mongodb --- #
        client = pymongo.MongoClient()
        database = client['news_project']
        news_coll = database.get_collection("new")

        #fetch data
        cursor=news_coll.find()
        ids=[]
        classes=[]
        merged_title_content=[]

        #loop documents
        for doc in cursor:
            ids.append(doc['_id'])
            classes.append(doc['fake'])
            merged_title_content.append(doc['title'] + '' + doc['body'])

         # --- Put collected information into a Json form (keys: ids, values: combined_title_content) --- #
            content_toJson={}
            for i,cid in enumerate(ids):
                content_toJson[cid]=merged_title_content[i]

        return {'content':content_toJson.values(),'classe':classes}
    except Exception as ex:
        print(ex)

data_output = getDataFromDb()



# --- Put the list of combined_title_data from a list of text into a string format --- #
def putIntoString(listOfText):
    string_text = ''.join(listOfText)
    return string_text

# --- Function to put our collected data into a pandas DataFrame --- #
def putDataInDataFrame():
    content_list = data_output['content']
    data_df = pd.DataFrame(content_list,columns=['content'])
    return data_df

# --- Function to clean the data --- #
def cleanData(text):
    text = re.sub('\[.*?\]', '', text) # Remove everything between []
    text = re.sub('\(.*?\)', '', text) # Remove everything between ()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # Remove punctuation
    text = re.sub('\w*\d\w*', '', text) # Remove numbers
    text = re.sub('[‘’“”«»…]', '', text) # Remove specific caracters
    text = re.sub("-_،؟ ً َّ ًّ ّ ٌّ َ ً ُ ٌ ٍ ِ ْ ٍّ ِّ", '', text) # Remove specific arabic caracters
    text = re.sub('\n', '', text) # Remove '\n'
    return text


# --- Function to organize the Dataframe (adding scores and classes columns) --- #
def organizeData(data_df,classes,cleaned_data):
    # --- Adding class column to dataframe --- #
    data_df['classe'] = classes
    data_df=data_df.sample(frac = 1)
    return data_df


#Training Models
class TrainingModels():
    def train(organizeData):
        organizeData.reset_index(drop=True, inplace=True)  # Remove dataframe indexes
        Y=organizeData['classe']
        X=organizeData.drop(columns=['classe']) # on supprime la colonne classe
        X=X['content']
        #splitting data into train & test data
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)
        pipe = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('model', SVC())])
        # Learning algorithm used : Support Vector Machine (SVM)
        #fitting
        model=pipe.fit(X_train,Y_train)

        #saving model
        pickle.dump(model, open('model.sav', 'wb'))
        #Predictions
        prediction = model.predict(X_test)
        #print(prediction)

        # Accuracy calcul
        #print("SVC accuracy: {}%".format(round(accuracy_score(Y_test, prediction) * 100, 2)))
        return model

        # --- Prediction function --- #

    def predict(text):
        data = getDataFromDb()['content']
        data_df = putDataInDataFrame()
        data_cleaning = lambda x: cleanData(x)

        # --- Organizing data in a pandas dataframe --- #
        cleaned_data = pd.DataFrame(data_df.content.apply(data_cleaning))
        organized_data = organizeData(data_df, getDataFromDb()['classe'], cleaned_data)
        # --- Training data --- #
        model = TrainingModels.train(organized_data)
        prediction = model.predict([text])
        print(prediction)
        return prediction[0]

'''
if __name__ == '__main__':
    getDataFromDb()
    prediction = TrainingModels.predict("منظمة الصحة العالمية لم تصرح بأن فيروس كورونا سينتهي في شهر ابريل سواء مع اللقاح أو بدونه")


    print(prediction[0])'''