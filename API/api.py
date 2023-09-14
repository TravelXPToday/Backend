from flask import Flask
from routes import bp as routes_bp
import re
from datetime import date
import datetime

from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run()

client = MongoClient('YOUR_CONNECTION_STRING')