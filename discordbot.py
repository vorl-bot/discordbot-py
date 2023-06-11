from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!', reference=message)

@client.event
async def gacha(message):
    if message.content.startswith(f'{PREFIX}가챠'):
        items = ['A','B','C','D']

        index = random.randrange(0,len(items))
        item = items[index]
        await message.channel.send(f'뾰로롱...! {item}이(가) 나왔다!', reference=message)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")