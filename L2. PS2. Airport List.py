#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "./data/options.html"


def extract_airports(page):
    data = []
    
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find(id='AirportList').findAll('option')    
        for i in range(len(items)):
            if 'All' in items[i]['value']:
                continue
            data.append(items[i]['value'])
            
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

    print "test was successful!"
    
if __name__ == "__main__":
    test()
