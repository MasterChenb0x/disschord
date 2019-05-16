#!/usr/local/bin/python3

from bs4 import BeautifulSoup as bs
import requests 

def infosec_news():
    """
    Grab InfoSec News from seclists.org
    """
    news = []
    r = requests.get("https://seclists.org/rss/isn.rss")
    r = r.text.encode("ascii", "ignore")
    soup = bs(r, "lxml")
    headlines = soup.find_all('title')

    for headline in headlines:
        news.append(headline.contents)

    return news

