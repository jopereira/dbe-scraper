#!/usr/bin/env python

import urllib.request
from random import randint
from time import sleep

agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

proxies = {'http': 'http://localhost:3128', 'https': 'https://localhost:3128'}
proxy_support = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

line = 1
f = open("list.txt","rt")
for url in f.readlines():

    url=url.strip()

    print("downloading", line, url)
    retries = 0

    while True:
        try:
            print("backoff...")
            sleep(randint(0,60))
            print("requesting...")

            headers = {'User-Agent': agents[randint(0,len(agents)-1)]}
            req = urllib.request.Request(url, None, headers)

            with urllib.request.urlopen(req) as response:
                the_page = response.read()
                name = "output/"+url[len('https://db-engines.com/en/system/'):]+".html"
                fo = open(name, "wt")
                fo.write(str(the_page))
                fo.close()
                print("Got it", name)
                break
        except Exception as e:
            print(str(e))
            print("Retrying...")
            retries +=1
             
            if retries >= 10:
                exit(1)

    line += 1