#!/usr/local/bin/python3

import random
import sys

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

    return response[random.randint(1, len(response))]

def grab_koan():
    """
    Grabs a zen koan from the koans.txt list (from ashidakim.com) and share it
   """
    koans = []
    with open('koans.txt', 'r') as f:
        for x in f:
            koans.append(x)
    return koans[random.randint(1, len(koans))]

def bro_code():
    """
    Grabs a rule of The Bro Code
    """
    brocode = []
    with open('brocode.txt', 'r') as f:
        for x in f:
            brocode.append(x)
    return brocode[random.randint(1, len(brocode))]

if __name__ == "__main__":
    print("This cannot be ran on its own!")
    sys.exit()
