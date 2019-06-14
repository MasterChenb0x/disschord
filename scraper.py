#!/usr/local/bin/python3

# I use this file as a separate space for web scraping. It will change depending on what the last scrape was.

import requests
from bs4 import BeautifulSoup as bs

url = "http://arstechnica.com/tag/security/"
r = requests.get(url)
soup = bs(r.content, "lxml")

for h in soup.find_all("h2"):
    for l in h.find_all("a"):
        print(f"{l.text}: {l.get('href')}")
