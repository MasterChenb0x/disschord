#!/usr/local/bin/python3

# I use this file as a separate space for web scraping. It will change depending on what the last scrape was.

import requests
from bs4 import BeautifulSoup as bs

url = "https://apod.nasa.gov/apod/astropix.html"

r = requests.get(url)
soup = bs(r.content, "lxml")

for link in soup.find_all("a"):
    print(link)
