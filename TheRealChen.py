#!/usr/local/bin/python3

#Import the universe
import discord
from command_functions import *
from weather_functions import *
from statz_gamez import *

#Read tokens from file
DISCORD_TOKEN = open("token.txt", "r").read().splitlines()

#-- Functions

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"-------")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if message.author == client.user:
        return

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
    

client.run(DISCORD_TOKEN[0])
