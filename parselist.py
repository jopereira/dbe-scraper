#!/usr/bin/env python

from bs4 import BeautifulSoup
from random import shuffle

f = open("list.html", "rt")
soup = BeautifulSoup(f, "html.parser")

table = soup.find('table', class_='dbi')

urls = []
cnt = -3
for row in table.find_all('tr'):
    cnt += 1
    if cnt<=0:
        continue
    url = row.find('th').find('a')['href']
    urls.append(url)

shuffle(urls)
for url in urls:
    print(url)
