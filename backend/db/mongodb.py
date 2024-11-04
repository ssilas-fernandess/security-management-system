from pymongo import MongoClient

def init_db(app):
    client = MongoClient('mongodb://mongo:27017')
    app.db = client["security_management"]
