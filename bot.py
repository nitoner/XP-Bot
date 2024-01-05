# This example requires the 'message_content' intent.

import discord
import os
import src
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)
