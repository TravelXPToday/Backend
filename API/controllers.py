from pymongo import MongoClient
import Utils.config as config

# Initialize MongoDB client
client = MongoClient(config.CONN, tlsAllowInvalidCertificates=True)
db = client['Travelers']  
travelers_collection = db['traveler']  
journey_collection = db['Journeys']

def get_all_journey():
    journeys = list(journey_collection.find({}, {'_id': 0}))  
    return journeys

def get_all_travelers():
    travelers = list(travelers_collection.find({}, {'_id': 0}))  
    return travelers
