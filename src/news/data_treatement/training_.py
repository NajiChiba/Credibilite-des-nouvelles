import pandas as pd
import string
import re
import pymongo
from mongoengine import connect
import pickle
import numpy as np
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


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
        #merged_title_content=[]
        titles = []
        articles = []

        #loop documents
        for doc in cursor:
            ids.append(doc['_id'])
            classes.append(doc['fake'])
            titles.append(doc['title'])
            articles.append(doc['body'])

        return {'title':titles, 'text':articles,'label':classes}
    except Exception as ex:
        print(ex)

data_output = getDataFromDb()


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


def putDataInDataFrame():
    title_list = list(cleanData(title_) for title_ in data_output['title'])
    text_list = list(cleanData(text_) for text_ in data_output['text'])
    dict_data = {'title':title_list, 'text': text_list, 'label':data_output['label']}
    data_df = pd.DataFrame(dict_data).sample(frac = 1)
    return data_df

class TrainingModel:
    def test_news(text):
        train = putDataInDataFrame()
        '''print('1----')
        print(train.shape)
        print('2----')'''
        print(train.head())
        print(train.isnull().sum())

        labels = train.label
        # print(labels.head())

        # DataFlair - Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(train['text'], labels, test_size=0.2, random_state=7)

        # DataFlair - Initialize a TfidfVectorizer
        tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

        # DataFlair - Fit and transform train set, transform test set
        tfidf_train = tfidf_vectorizer.fit_transform(X_train)
        tfidf_test = tfidf_vectorizer.transform(X_test)

        # DataFlair - Initialize a PassiveAggressiveClassifier
        pac = PassiveAggressiveClassifier(max_iter=50)
        pac.fit(tfidf_train, y_train)

        # DataFlair - Predict on the test set and calculate accuracy
        y_pred = pac.predict(tfidf_test)
        score = accuracy_score(y_test, y_pred)
        # print(f'Accuracy: {round(score * 100, 2)}%')

        # get the data from test dataset and get final predictions
        tfidf_test = tfidf_vectorizer.transform([text])
        final_predictions = pac.predict(tfidf_test)
        print('result ---- ')
        print(final_predictions)
        return final_predictions

model_ = TrainingModel()
'''
res = test_news("هذا الفيديو قديم والأشخاص فيه لا يحطمون الأصنام لأنها لم تساعدهم في الشفاء من فيروس كورونا")

print(res)'''