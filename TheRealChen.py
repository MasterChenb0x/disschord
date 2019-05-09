#!/usr/local/bin/python3

#Import the universe
import discord

#Read token from file
TOKEN = open("token.txt", "r").read().splitlines()

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"-------")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    

client.run(TOKEN[0])
