#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json
import pprint
from zipfile import ZipFile

html_page = "./data/page.html"
html_option = "./data/option.html"

def extract_data(html):
    data = {"eventvalidation": "",
            "viewstate": "",
            "airports": [],
            "carriers":[] }
    #with open(page, "r") as html:
        # do something here to find the necessary values
    soup = BeautifulSoup(html, 'html.parser')
    ev = soup.find(id='__EVENTVALIDATION')
    data['eventvalidation'] = ev['value']
    vs = soup.find(id='__VIEWSTATE')
    data['viewstate'] = vs['value']
        #pass

    items = soup.find(id='CarrierList').findAll('option')    
    for i in range(len(items)):
        if 'All' in items[i]['value']:
            continue
        data['carriers'].append(items[i]['value'])

    items = soup.find(id='AirportList').findAll('option')    
    for i in range(len(items)):
        if 'All' in items[i]['value']:
            if items[i]['value'] == 'AllOthers': # only handle all major 
                break
            continue
        data['airports'].append(items[i]['value'])
        
    return data

def make_request(req, data, airport=None, carrier=None):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airports = data["airports"]
    carriers = data["carriers"]
    
    r = req.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': airports,
                          'CarrierList': carriers,
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    #data = extract_data(html_page)
    #assert data["eventvalidation"] != ""
    #assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    #assert data["viewstate"].startswith("/wEPDwUKLTI")

    s = requests.Session()
    r = s.get('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2')
    #html = open('data/bts.html', "w")
    #html.write(r.text)
    #html.close()
        
    data = extract_data(r.text)
    res = make_request(s, data)
    f = open('AllMajor.html', 'w')
    f.write(res)
    f.close()
    #print len(data['airports'])

    '''                   
    for airport in data["airports"]:
        for carrier in data["carriers"]:
            res = make_request(s, data, airport, carrier)
            name = str(airport) + '-' + str(carrier) + '.html'
            f = open('{}/{}'.format('data/bts', name), 'w')
            print name
            f.write(res)
            f.close()
    '''           

def open_zip(datadir=None):
    with ZipFile('{0}.zip'.format('./data/bts_major'), 'r') as myzip:
        myzip.extractall('./data/bts_major')
        
#test()
open_zip()
