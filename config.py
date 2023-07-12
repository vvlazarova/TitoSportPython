import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xa5\xf0\x15_\x8d\xbfn\xd0\xce\x12\x07\xa3\xa0\xcet\xc6'

    MONGODB_SETTINGS = { 'db' : 'Users' }
