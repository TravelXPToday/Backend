<img src="https://flask.palletsprojects.com/en/2.3.x/_images/flask-horizontal.png" alt="Italian Trulli">

# Back-end


![GitHub Actions Workflow Status](https://github.com/TravelXPToday/Backend/workflows/Python%20application/badge.svg)
![GitHub Actions Workflow Status](https://github.com/TravelXPToday/Backend/workflows/Build%20and%20Push%20to%20Docker%20Hub/badge.svg)


![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)
![Code Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![GitHub last commit](https://img.shields.io/github/last-commit/TravelXPToday/Backend)
![GitHub repo size](https://img.shields.io/github/repo-size/TravelXPToday/Backend)
![GitHub top language](https://img.shields.io/github/languages/top/TravelXPToday/Backend)
![GitHub language count](https://img.shields.io/github/languages/count/TravelXPToday/Backend)
![GitHub contributors](https://img.shields.io/github/contributors/TravelXPToday/Backend)
![GitHub open issues](https://img.shields.io/github/issues-raw/TravelXPToday/Backend)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/TravelXPToday/Backend)


### Flask
Why whe chose Flask:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

- We might want to integrate AI what is easier with Flask because it runs on Python.

## Security 

We made a config.py file that has the connection string to the database. This file is in the .gitignore so it is not visible on GitHub.
We added sonar cloud to the project to check for vulnerabilities and bad code.  
# Tests
We started making [Unit Tests]  they can be found here : [[TravelXPToday Back-end Testing]].

### how to start the program
To run the React app, run the following commands in the terminal:
```bash
cd TravelXPToday
npm install
npm start
```
To run the Flask app, run the following commands in the terminal:
```bash
cd API
pip install -r requirements.txt
python app.py
```
---
# File Structure:
```mermaid
classDiagram

  

    class api {

        +Flask App Initialization

        +CORS Configuration

    }

  

    class routes {

        +http://127.0.0.1:5000/journey/all (GET)

        +http://127.0.0.1:5000/journey (POST)

        +http://127.0.0.1:5000/journey (PUT)

        +http://127.0.0.1:5000/journey (DELETE)

        +http://127.0.0.1:5000/traveler/all (GET)

        +http://127.0.0.1:5000/traveler (POST)

        +http://127.0.0.1:5000/traveler (PUT)

        +http://127.0.0.1:5000/traveler (DELETE)

    }

  

    class controllers {

        +get_all_travelers()

        +create_traveler(data)

        +update_traveler(criteria, updates)

        +delete_traveler(criteria)

        +get_all_journeys()

        +create_journey(data)

        +update_journey(criteria, updates)

        +delete_journey(criteria)

    }

  

    class CRUDInterface {

        +create(data)

        +read(criteria)

        +update(criteria, updates)

        +delete(criteria)

    }

  

    class DataAccess {

        +create(data)

        +read(criteria=)

        +update(criteria, updates)

        +delete(criteria)

    }

  

    class Traveler {

        +__init__()

    }

  

    class Journey {

        +__init__()

    }

  

    api --> routes

    routes --> controllers

    controllers --> Traveler

    controllers --> Journey

    Traveler --|> CRUDInterface

    Traveler --|> DataAccess

    Journey --|> CRUDInterface

    Journey --|> DataAccess
```
This is a Diagram of our application it is prone to change in the future.

## api.py

```python

from flask import Flask, jsonify
from flask_cors import CORS
from routes import bp as routes_bp
import Utils.config as config
from flask import Flask, render_template
# Initialize Flask app
server = Flask(__name__)
CORS(server)
server.register_blueprint(routes_bp)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT, debug=True)


```
Here we set up the server and register the routes. 
## controller.py

```python

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


```

Here we will implement the logic needed for the application and will set the criteria for the database. We also define the functions to get all the data from the database.
## routes.py

```python

from flask import Blueprint, jsonify, request
from flask import Flask, render_template
from controllers import (
    get_all_journeys, get_all_travelers,
    create_journey, create_traveler,
    update_journey, update_traveler,
    delete_journey, delete_traveler
)

bp = Blueprint('routes', __name__)

@bp.route('/')
def mermaid_diagram():
    return render_template('index.html')

@bp.route('/journey/all', methods=['GET'])
def journey():
    return jsonify(get_all_journeys())

@bp.route('/journey', methods=['POST'])
def add_journey():
    data = request.json
    create_journey(data)
    return jsonify({"message": "Journey added successfully!"})

@bp.route('/journey', methods=['PUT'])
def modify_journey():
    criteria = request.args.to_dict() 
    updates = request.json
    update_journey(criteria, updates)
    return jsonify({"message": "Journey updated successfully!"})

@bp.route('/journey', methods=['DELETE'])
def remove_journey():
    criteria = request.args.to_dict()  
    delete_journey(criteria)
    return jsonify({"message": "Journey deleted successfully!"})

@bp.route('/traveler/all', methods=['GET'])
def travelers():
    return jsonify(get_all_travelers())

@bp.route('/traveler', methods=['POST'])
def add_traveler():
    data = request.json
    create_traveler(data)
    return jsonify({"message": "Traveler added successfully!"})

@bp.route('/traveler', methods=['PUT'])
def modify_traveler():
    criteria = request.args.to_dict() 
    updates = request.json
    update_traveler(criteria, updates)
    return jsonify({"message": "Traveler updated successfully!"})

@bp.route('/traveler', methods=['DELETE'])
def remove_traveler():
    criteria = request.args.to_dict()  
    delete_traveler(criteria)
    return jsonify({"message": "Traveler deleted successfully!"})

```
Here we define the routes for the API. We use the functions from the controller to get the data from the database and return it as JSON.
 
## DataAccess.py

```python
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
        return list(self.collection.find(criteria, {'_id': 0}))

    def update(self, criteria, updates):
        return self.collection.update_many(criteria, {'$set': updates})

    def delete(self, criteria):
        return self.collection.delete_many(criteria)

```
Here we access the database.
## Object classes journey.py and traveler.py

```python
from data_access import DataAccess
from crud_interface import CRUDInterface

class Traveler(DataAccess, CRUDInterface):
    def __init__(self):
        super().__init__('traveler')

# journey.py
from data_access import DataAccess
from crud_interface import CRUDInterface

class Journey(DataAccess, CRUDInterface):
    def __init__(self):
        super().__init__('Journeys')
```
## crud_interface.py

```python
from abc import ABC, abstractmethod

class CRUDInterface(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, criteria):
        pass

    @abstractmethod
    def update(self, criteria, updates):
        pass

    @abstractmethod
    def delete(self, criteria):
        pass
```
Interface to make sure the correct elements are there for the project to work.

# Testing 


## Unit Tests
Keep in mind to put them in the /tests directory in the main of the project.
Example:
```
API
|	/Test
|	|	crudtests.py 
|	api.py
```

```python 
import unittest
import logging
from unittest.mock import patch
from controllers import create_traveler, create_journey, get_all_travelers, get_all_journeys, update_traveler, update_journey, delete_traveler, delete_journey
# python -m unittest discover tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestControllers(unittest.TestCase):
    @patch('controllers.Traveler.read')
    def test_get_all_travelers(self, mock_read):
        logger.info("\nRunning test_get_all_travelers test case")
        mock_data = [{"name": "Art"}, {"name": "Jelle"}]
        mock_read.return_value = mock_data

        result = get_all_travelers()
        self.assertEqual(result, mock_data)
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")
    
    @patch('controllers.Traveler.create')
    def test_create_traveler(self, mock_create):
        logger.info("\nRunning test_create_traveler test case")
        mock_data = {
            "name": "Art",
            "age": 30,
            "destination": "London"
        }
        mock_response = {"inserted_id": "5f4abc56e12b5c34a3c5821e"}
        mock_create.return_value = mock_response

        result = create_traveler(mock_data)
        self.assertEqual(result["inserted_id"], mock_response["inserted_id"])
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Traveler.update')
    def test_update_traveler(self, mock_update):
        logger.info("\nRunning test_update_traveler test case")
        criteria = {"name": "Art"}
        updates = {"age": 31}
        mock_response = {"modified_count": 1}
        mock_update.return_value = mock_response

        result = update_traveler(criteria, updates)
        self.assertEqual(result["modified_count"], mock_response["modified_count"])
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Updates: {updates}")
        logger.debug(f"Result: {result}")


    @patch('controllers.Traveler.delete')
    def test_delete_traveler(self, mock_delete):
        logger.info("\nRunning test_delete_traveler test case")
        criteria = {"name": "Art"}
        mock_delete.return_value = None

        result = delete_traveler(criteria)
        self.assertIsNone(result)
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Result: {result}")


    @patch('controllers.Journey.read')
    def test_get_all_journeys(self, mock_read):
        logger.info("\nRunning test_get_all_journeys test case")
        mock_data = [
            {"origin": "Paris", "destination": "London", "travel_date": "2023-09-22"},
            {"origin": "London", "destination": "Berlin", "travel_date": "2023-09-25"}
        ]
        mock_read.return_value = mock_data

        result = get_all_journeys()
        self.assertEqual(result, mock_data)
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Journey.create')
    def test_create_journey(self, mock_create):
        logger.info("\n Running test_create_journey test case")
        mock_data = {
            "origin": "Paris",
            "destination": "London",
            "travel_date": "2023-09-22"
        }
        mock_response = {"inserted_id": "5f4abc56e12b5c34a3c5821e"}
        mock_create.return_value = mock_response

        result = create_journey(mock_data)
        self.assertEqual(result["inserted_id"], mock_response["inserted_id"])
        logger.debug(f"Mocked data: {mock_data}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Journey.update')
    def test_update_journey(self, mock_update):
        logger.info("\nRunning test_update_journey test case" )
        criteria = {"origin": "Paris", "destination": "London"}
        updates = {"travel_date": "2023-09-23"}
        mock_response = {"modified_count": 1}
        mock_update.return_value = mock_response

        result = update_journey(criteria, updates)
        self.assertEqual(result["modified_count"], mock_response["modified_count"])
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Updates: {updates}")
        logger.debug(f"Result: {result}")

    @patch('controllers.Journey.delete')
    def test_delete_journey(self, mock_delete):
        logger.info("\nRunning test_delete_journey test case")
        criteria = {"origin": "Paris", "destination": "London"}
        mock_delete.return_value = None

        result = delete_journey(criteria)
        self.assertIsNone(result)
        logger.debug(f"Criteria: {criteria}")
        logger.debug(f"Result: {result}")
```





