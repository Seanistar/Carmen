"""
Complete the insert_data function to insert the data into MongoDB.
"""

import json
import pprint

def insert_data(data, db):

    # Your code here. Insert the data into a collection 'arachnid'
    for entry in data:
        db.arachnid.insert(entry)

if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    # with open('../data/arachnid.json') as f:
    with open('../data/sts.json') as f:
        try:
            # data = json.loads(f.read())
            data = json.loads(f.read())
            # insert_data(data, db)
            # print db.arachnid.find_one()
            print data
        except ValueError as e:
            print e

