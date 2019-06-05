#!/usr/local/bin/python3

# I use this file as a separate space for web scraping. It will change depending on what the last scrape was.

import requests
from bs4 import BeautifulSoup as bs

url = "http://picount.com"

r = requests.get(url)
# soup = bs(r.content, "lxml")

print(r.json())
