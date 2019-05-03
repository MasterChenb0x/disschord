#!/usr/local/bin/python3

# Built by following https://www.devdungeon.com/content/make-discord-bot-python
# Work with Python 3.6
import discord
import random

def f_request(msg):
    with open("features.txt", "a") as f:
        f.write(str(msg) + "\n")

def ate_bawl():
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

TOKEN = 'YOUR_TOKEN'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

#--- OG Chen code ---#
    if message.content.startswith('!feature'):
        f_request(message.content)
        msg = 'Your request has been logged. Give my creator 3-4 weeks to implement your request.'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!8-ball'):
        msg = ate_bawl()
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
