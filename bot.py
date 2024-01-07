import discord
import os
import aiosqlite
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    #bot.db = await aiosqlite.connect('databases/xp.db')
    #cursor = await bot.db.cursor()
    #await cursor.execute('')
    await bot.load_extension(f"src.cogs.admin")
    synced = await bot.tree.sync()
    print(f'We have logged in as {bot.user}')
    print(f'{len(synced)} commands were synced')

bot.run(TOKEN)
