from pymongo import MongoClient
import Utils.config as config

# Initialize MongoDB client
client = MongoClient(config.CONN)
db = client['Travelers']  
travelers_collection = db['traveler']  

def get_journey():
    return {
        'name': 'alice',
        'email': 'alice@outlook.com'
    }

def get_all_travelers():
    travelers = list(travelers_collection.find({}, {'_id': 0}))  
    return travelers
