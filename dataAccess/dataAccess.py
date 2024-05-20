"""
dataAccess.py

This module establishes a connection to the MongoDB database using pymongo.

Modules Imported:
    - pymongo.MongoClient: MongoClient class for connecting to MongoDB.

Global Variables:
    - db: MongoDB database instance.


"""

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Select database
db = client['BalanceDB']
