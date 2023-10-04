from pymongo import MongoClient
import Utils.config as config

class DataAccess:
    def __init__(self, collection_name):
        client = MongoClient(config.CONN, tlsAllowInvalidCertificates=True)
        db = client['Travelers']
        self.collection = db[collection_name]

    def create(self, data):
        return self.collection.insert_one(data)

    def read(self, criteria={}):
        data = list(self.collection.find(criteria))
        for item in data:
            item['_id'] = str(item['_id'])  
        return data


    def update(self, criteria, updates):
        return self.collection.update_many(criteria, {'$set': updates})

    def delete(self, criteria):
        return self.collection.delete_many(criteria)
