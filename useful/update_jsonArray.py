#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import pprint

def parse_array(v):
    if type(v) == float:
        return [v]
    
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [float(i.strip()) for i in v_array]
        return v_array

    return [v]

def update_db(data, db):

    for entry in data:
        value1, value2 = [], []
        try:
            # value = parse_array(entry['isPartOf_label'])
            # db.cities.update({'name':entry['name']},{"$set":{'isPartOf':value}})
            # value = parse_array(entry['name'])
            # db.cities.update({'rdf-schema#label':entry['rdf-schema#label']},{"$set":{'name':value}})
            #value1 = parse_array(entry['wgs84_pos#long'])
            #value2 = parse_array(entry['wgs84_pos#lat'])
            lat,lon = float(entry['wgs84_pos#lat'][0]), float(entry['wgs84_pos#long'][0])
            db.cities.update({'rdf-schema#label':entry['rdf-schema#label']},{"$set":{'wgs84_pos#long':lon,'wgs84_pos#lat':lat } } )
        except:
            print 'updating failed...'

def find_data(db):
        
    data = db.cities.find({})

    return data
    
    
def test():
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client['examples']

    data = find_data(db)
    update_db(data, db)

    # pprint.pprint(data)
    print "updating is successufl!"
    
if __name__ == "__main__":
    test()
