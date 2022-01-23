from pymongo import MongoClient


class Db_conn():
    def __init__(self):
        client = MongoClient()
        self.db = client['news_project']
        self.new_coll = self.db.new
        
    def insert_elem(self, article):
        result = self.new_coll.insert_one(article)
        
        print("\n\n\n----------------------")
        print("First article key is: {}".format(result.inserted_id))
        print("----------------------\n\n\n")

    def test(self):
        print(self.db)



def main_prog():
    article = {
                "title": "Article ajouté par python --2--",
                "body": "loreampson articl was added by python from functio insert_elem"
            }
    db = Db_conn()
    db.insert_elem(article)

if  __name__ == '__main__':
    main_prog()
















'''def add_to_db():
    article = {
                "title": "Article ajouté par python",
                "body": "loreampson articl was added by python from functio insert_elem"
            }
    my_collection = Db_conn()
    my_collection.insert_elem(article)
    my_collection.test()

'''