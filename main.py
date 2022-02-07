from dotenv import load_dotenv
from discord.ext import commands
import discord
import os

load_dotenv()

token = os.getenv("discord_token")
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Bot is ready")
    

try:
    bot.run(token)
except Exception as e:
    print(f"Error in {e}")