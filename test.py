import os, re, json, asyncio, traceback, datetime, math, pytz, time
import discord
from io import BytesIO
from discord.ext import commands, tasks

TOKEN = ('')
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='..', intents=intents)
bot.load_extension('EventLeaderboard.EventLeaderboard')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mod apps!"))

bot.run(TOKEN)