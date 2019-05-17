#!/usr/local/bin/python3

# I use this file as a separate space for web scraping. It will change depending on what the last scrape was.

import requests
from bs4 import BeautifulSoup as bs

with open("brocode.txt", "a") as f:
    for num in range(1,8):
        url = f"https://brocode.org/the-code/{num}/"

        r = requests.get(url)
        r = r.text.encode("ascii", "ignore")
        soup = bs(r, "lxml")

        for link in soup.find_all("a"):
            f.write(link.text + "\n")


"""
for d in soup.find_all("div", {'class':'main-code-box'}):
    print(soup.find_all("a"))
"""
