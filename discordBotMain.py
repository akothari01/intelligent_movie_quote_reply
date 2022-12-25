import discord
import Main as M
import os
import json
import random
from discord.ext import commands


if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)


TOKEN = configData["Token"]
prefix = configData["Prefix"]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if ctx.command in bot.commands:
        await bot.process_commands(message)
        return
    if message.author == bot.user:
        return
    text = M.handleMessage(message.content)
    if random.randint(0, 100) <= 20:
        await message.channel.send(text)


@bot.command()
async def kill(ctx):
    await ctx.send(f'you killed me in cold blood {ctx.author}')
    exit()


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot commands',
        description='this is the shit i can do',
        color=discord.Colour.magenta()
    )
    embed.add_field(
        name='!help',
        value='so you called me without knowing what i do?????',
        inline=False
    )
    embed.add_field(
        name='!kill',
        value='if i could i would kill myself but since i cant youll have to do',
        inline=False
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)