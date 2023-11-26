#!/usr/bin/env python

from bs4 import BeautifulSoup
from sys import argv

def mytext(e):
    x = e.find(text=True, recursive=False)
    return x

histo = {}

for fn in argv[1:]:
    f = open(fn, "rt")
    soup = BeautifulSoup(f, "html.parser")
    f.close()

    table = soup.find('table', class_='tools')

    for row in table.find_all('tr'):
        tds = row.find_all('td')

        if mytext(tds[0]) == 'Name':
            name = mytext(tds[1])
        if mytext(tds[0]) == 'Initial release':
            initial = mytext(tds[1])

    initial = int(initial)
    cnt = histo.get(initial,[])
    cnt.append(name)
    histo[initial] = cnt

for k in histo:
    print(k,len(histo[k]))
