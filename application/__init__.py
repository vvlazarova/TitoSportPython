# File: __init__.py
# Author: Violeta Lazarova
# Description: This file initializes the Flask app and sets up the 
# database connection using Flask-MongoEngine.

from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the MongoEngine database
db = MongoEngine()
db.init_app(app)

# Import the routes module to ensure the routes are registered
from application import routes

