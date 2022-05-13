#============================================
# Title: Exercise 9.3
# Author: Professor Krasso
# Date: 12 May 2022
# Modified By: Laura Kendl
# Description: This program demonstrates how to
# query and create documents in a MongoDB database
# instance through Python and pymongo.
# Resources:
# [Ref A] Blackboard: Exercise 9.2 Instructions (Professor Krasso)
# [Ref B] Geeksforgeeks: https://www.geeksforgeeks.org/python-mongodb-find_one-query/ (Python MongoDB – find_one Query)
# ===========================================

# Import statements.
from pymongo import MongoClient
import pprint
import datetime

# Connect to local MongoDB instance.
client = MongoClient('localhost', 27017)
db = client.web335

# Update user document.
db.users.update_one(
    {"employee_id": "0000008"},
    {
        "$set": {
            "email": "lkendl@my365.bellevue.edu"
        }
    }
)

# Query the users collection and output email, employee_id, first_name and last_name.
pprint.pprint(db.users.find_one({"employee_id": "0000008"}, {"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1, "date_created": 0}))