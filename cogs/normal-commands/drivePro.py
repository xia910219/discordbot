from re import purge
from disnake.ext import commands
from disnake.ext.commands import *
import disnake
import json

class dirvePro(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ht(self, ctx, msg, httpUrl):
        print(msg)
        print(httpUrl)
        channel = self.bot.get_channel(940939714679164928)
        await channel.send(httpUrl)
                


def setup(bot):
    bot.add_cog(dirvePro(bot))