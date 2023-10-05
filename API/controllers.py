from traveler import Traveler
from journey import Journey

def get_all_travelers():
    traveler = Traveler()
    return traveler.read()

def create_traveler(data):
    traveler = Traveler()
    return traveler.create(data)

def update_traveler(criteria, updates):
    traveler = Traveler()
    return traveler.update(criteria, updates)

def delete_traveler(criteria):
    traveler = Traveler()
    return traveler.delete(criteria)

def get_all_journeys():
    journey = Journey()
    return journey.read()

def create_journey(data):
    journey = Journey()
    return journey.create(data)

def update_journey(criteria, updates):
    journey = Journey()
    return journey.update(criteria, updates)

def delete_journey(criteria):
    journey = Journey()
    return journey.delete(criteria)

def read_journey_by_id(id):
    journey = Journey()
    return journey.readById(id)

# blalbalbal
