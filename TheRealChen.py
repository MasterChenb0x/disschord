#!/usr/local/bin/python3

#Import the universe
import discord
from command_functions import *
from weather_functions import *
from chatter_functions import *
from statz_gamez import *
import random

#Read tokens from file
DISCORD_TOKEN = open("token.txt", "r").read().splitlines()

#-- Functions

client = discord.Client()
lastmsg = "i will fight you"

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"-------")


@client.event
async def on_message(message):
    global lastmsg
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if message.author == client.user: # Ignore messages sent from self.
        return

#-- Random Chatter message. Most likely to be moved elsewhere later.
#    if (random.randint(1000, 99991231) + xOrShift()) % 300 < 1:
    saysomething = random.randint(1,2436)
    if saysomething % 9 == 1:
        await message.channel.send(bro_code())
#-- End random chatter

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

#--- OG Chen code ---#
    if message.content.startswith('!feature'):
        f_request(message.content)
        msg = 'Your request has been logged. Give my creator 3-4 weeks to implement your request.'
        await message.channel.send(msg)

    if message.content.startswith('!8-ball'):
        msg = ate_bawl()
        await message.channel.send(msg)

    if message.content.startswith('!zen'):
        msg = 'Here\'s a zen story for you.'
        await message.channel.send(msg)
        msg = grab_koan()
        await message.channel.send(msg)

    if message.content.startswith('!brocode'):
        msg = 'Always mind The Bro Code.'
        await message.channel.send(msg)
        msg = bro_code()
        await message.channel.send(msg)

    if message.content.startswith('!weather'):
        query = message.content.split(" ")
        city = " ".join(query[1:])  
        msg = get_weather(city)
        #msg = city
        await message.channel.send(msg)

    if message.content.startswith("!dice"):
        query = message.content.split(" ")
        await message.channel.send(dice_roll(int(query[1])))

    if message.content.startswith("!coinflip"):
        await message.channel.send(coin_flip())
    
    if message.content.startswith("!news"):
        news = infosec_news()
        for x in news:
            await message.channel.send(x)

    if message.content.startswith("!help"):
        await message.channel.send(help())

#-- Not ready until I can track last message
    if message.content.startswith("!mock"):
        msg = mock(lastmsg)
        await message.channel.send(msg)
    lastmsg = message.content

client.run(DISCORD_TOKEN[0])

