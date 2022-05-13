#============================================
# Title: Exercise 9.2
# Author: Professor Krasso
# Date: 12 May 2022
# Modified By: Laura Kendl
# Description: This program demonstrates how to
# query and create documents in a MongoDB database
# instance through Python and pymongo.
# Resources:
# Blackboard: Exercise 9.2 Instructions (Professor Krasso)
# ===========================================

# Import statements.
from pymongo import MongoClient
import pprint
import datetime

# Connect to local MongoDB instance.
client = MongoClient('localhost', 27017)
db = client.web335

# Create a new user document.
user = {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}

# Insert the new user document.
user_id = db.users.insert_one(user).inserted_id

# Output the auto-generated user_id.
print(user_id)

# Query the users collection using "find_one()" method and print document.
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))