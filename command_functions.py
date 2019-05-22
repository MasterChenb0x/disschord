#!/usr/local/bin/python3

import random
import sys
from bs4 import BeautifulSoup as bs
import requests


def help():
    return """ TheRealChen-bot by MasterChen
    !feature <request>
    !8-ball <question>
    !koan (grabs a zen story)
    !weather <city>

    """

def f_request(msg):
    """
    Logs a feature reuest from a user
    """
    with open("features.txt", "a") as f:
        f.write(str(msg) + "\n")

def ate_bawl():
    """
    Magic 8 Ball function
    """
    response = ['It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes - definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy, try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful']

    return response[random.randint(1, len(response)-1)]

def grab_koan():
    """
    Grabs a zen koan from the koans.txt list (from ashidakim.com) and share it
   """
    koans = []
    with open('koans.txt', 'r') as f:
        for x in f:
            koans.append(x)
    return koans[random.randint(1, len(koans)-1)]

def bro_code():
    """
    Grabs a rule of The Bro Code
    """
    brocode = []
    with open('brocode.txt', 'r') as f:
        for x in f:
            brocode.append(x)
    return brocode[random.randint(1, len(brocode)-1)]

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

def mock(message):
    """
    MoCk ThE lAsT mEsSaGe
    """
    new_string = []
    for char in range(0,len(message)):
        if char % 2 == 0:
            new_string.append(message[char].upper())
        else:
            new_string.append(message[char])
    return "".join(new_string)
    

if __name__ == "__main__":
    print("This cannot be ran on its own!")
    sys.exit()
