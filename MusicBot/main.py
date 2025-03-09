# Created by
# Credit = Aruvu (Livenser)
# Tanggal pembuatan = 3/9/2025
# Github = https://github.com/Livenser

#libray yang digunakan
import discord
import os
import asyncio
import random
import aiohttp
import yt_dlp as youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

# Sambungkan token di .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Integrasi Dengan bot Discord
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Aktifkan {bot.user}")
    await bot.tree.sync()
    print("Bot Sudah Siap Dipakai.")

# Load cog ekstensi music
async def load_extensions():
    await bot.load_extension("music")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())
