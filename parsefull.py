#!/usr/bin/env python

from bs4 import BeautifulSoup
from random import shuffle

f = open("fulllist.html", "rt")
soup = BeautifulSoup(f, "html.parser")

table = soup.find('table', class_='list')

urls = []
for row in table.find_all('a'):
    url = row['href']
    urls.append(url)

shuffle(urls)
for url in urls:
    print(url)
