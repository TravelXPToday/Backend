from flask import Flask, request, jsonify
from flask_cors import CORS
from routes import bp as routes_bp
import re
from datetime import date
import Utils.config as config
from flask import Flask, render_template, request
from pymongo import MongoClient


server = Flask(__name__)
CORS(server)
server.register_blueprint(routes_bp)

@server.route('/traveler', methods=['GET'])
def get_traveler():
    return jsonify(get_traveler()), 200

@server.route('/journey', methods=['GET'])
def get_journey():
    return jsonify(get_journey()), 200

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)

client = MongoClient(config.CONN)