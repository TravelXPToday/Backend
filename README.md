<img src="https://flask.palletsprojects.com/en/2.3.x/_images/flask-horizontal.png" alt="Italian Trulli">

# Back-end 

### Flask
Why whe chose Flask:

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
- We might want to integrate AI what is easier with Flask because it runs on Python.

## File Structure:

#### api.py

```python
# Initialize Flask app
server = Flask(__name__)
CORS(server)
server.register_blueprint(routes_bp)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
```

Here we set up the server and register the routes.

#### controller.py

```python
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
```

Here we set up the connection to the MongoDB database. We also define the functions to get all the data from the database.

#### routes.py

```python
bp = Blueprint('routes', __name__)

@bp.route('/journey/all', methods=['GET'])
def journey():
    return jsonify(get_all_journey())

@bp.route('/traveler/all', methods=['GET'])
def travelers():
    return jsonify(get_all_travelers())
```

Here we define the routes for the API. We use the functions from the controller to get the data from the database and return it as JSON.

## Security

We made a config.py file that has the connection string to the database. This file is in the .gitignore so it is not visible on GitHub.