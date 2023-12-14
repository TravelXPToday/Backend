from bson import ObjectId
from pymongo import MongoClient
import logging
import Utils.config as config

class DataAccess:
    def __init__(self, collection_name):
        client = MongoClient(config.CONN, tlsAllowInvalidCertificates=True)
        db = client['Travelers']
        self.collection = db[collection_name]

    def create(self, data):
        if 'traveler' in str(self):
            required_fields = ['Email', 'Username']
        elif 'journey' in str(self):
            required_fields = ['name', 'start_time', 'end_time', 'start_location', 'destination', 'mode_of_transport']
        else:
            required_fields = []

        if all(field in data for field in required_fields):
            return self.collection.insert_one(data)
        else:
            missing_fields = [field for field in required_fields if field not in data]
            log_message = f"Validation failed for data: {missing_fields}"
            logging.error(log_message)
            raise ValueError("Missing required information.")

    def read(self, criteria={}):
        data = list(self.collection.find(criteria))
        for item in data:
            item['_id'] = str(item['_id'])  
        return data

    def update(self, criteria, updates):
        return self.collection.update_many(criteria, {'$set': updates})

    def delete(self, criteria):
        return self.collection.delete_many(criteria)
    
    def readById(self, id):
        object_id = ObjectId(id)
        data = self.collection.find_one({'_id': object_id})
        data['_id'] = str(data['_id'])
        return data
