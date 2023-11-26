#!/usr/bin/env python

from bs4 import BeautifulSoup
from sys import argv
from json import dumps

def mytext(e):
    x = e.find(text=True, recursive=False)
    return x

data = []

for fn in argv[1:]:
    f = open(fn, "rt")
    soup = BeautifulSoup(f, "html.parser")
    f.close()

    table = soup.find('table', class_='tools')

    entry = {}
    for row in table.find_all('tr'):
        tds = row.find_all('td')
        key = mytext(tds[0])

        if key == "Editorial information provided by DB-Engines":
            continue
        value = None
        try:
            value = mytext(tds[1])
        except:
            pass
        if key and value:
            entry[key.strip()] = value.strip()

    data.append(entry)

print(dumps(data, indent=4))