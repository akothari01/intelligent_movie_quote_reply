import discord
import Main as M
import os
import json


if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)


TOKEN = configData["Token"]
prefix = configData["Prefix"]
intents = discord.Intents.all()
client = discord.Client(command_prefix=prefix, intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print('message --->', message)
    if message.author == client.user:
        return
    text = M.handleMessage(message.content)
    await message.channel.send(text)


client.run(TOKEN)
