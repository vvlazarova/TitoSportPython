# File: config.py
# Author: Violeta Lazarova
# Description: This file contains the configuration class for the Flask app.
# It defines the secret key and MongoDB settings used by the app.

import os

class Config(object):
    # Define the secret key for the Flask app
    # Retrieve the value from the environment variable 'SECRET_KEY'
    # If the environment variable is not set, use the provided default value
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xa5\xf0\x15_\x8d\xbfn\xd0\xce\x12\x07\xa3\xa0\xcet\xc6'

    # Configure the MongoDB settings for the Flask app
    # Set the MongoDB database name to 'Users'
    MONGODB_SETTINGS = { 'db' : 'Users' }
