from dotenv import load_dotenv
from disnake.ext import commands
import discord
import os

load_dotenv()

token = os.getenv("discord_token")
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Bot is ready")
    

def load_commands(command_type: str) -> None:
    for file in os.listdir(f"./cogs/{command_type}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Load extension {extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"fail to load extension {extension}\n{exception}")
    
if __name__ == "__main__":
    load_commands("normal-commands")
    load_commands("stone-commands") 


bot.run(token)