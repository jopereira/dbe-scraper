# DBEngines scraper

## Downloading

1. save https://db-engines.com/en/systems as fulllist.html

2. parsefull.py > list.txt

3. docker run --rm -it -p 3128:3128 zhaowde/rotating-tor-http-proxy

4. download.py

5. kill docker container

6. tojson.py output/*.html > dbengines.json

## Some statistics

bydate.py output/*.html > bydate.csv
