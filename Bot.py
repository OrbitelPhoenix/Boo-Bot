import asyncio
import glob
import json
import random
import time
import aiohttp
import imageio
import io
import os
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = ("*", "@Boo")
TOKEN = 'NDk3NTYyMjQxODczNDc3NjQy.DuyOMQ.lxWtBTxpIWz3PNnfp8GEUluyBOY'

client = Bot(command_prefix=BOT_PREFIX)



@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Luigi's Mansion"))
    

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))



@client.command(description=" Say's Helo ",
                aliases=['HI', 'hi', 'HELO', 'Helo', 'helo',],
                pass_context=True)
async def Hi(context):
    await client.say(("Ha Ha, Hi ") + context.message.author.mention)



async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
