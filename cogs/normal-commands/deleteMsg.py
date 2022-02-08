from re import purge
from disnake.ext import commands
from disnake.ext.commands import *
import disnake

class DeleteMsg(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def clear(self, ctx, nums : int):
        try:
            await ctx.channel.purge(limit = nums + 1)
        except Exception as e:
            await ctx.send(str(e))


def setup(bot):
    bot.add_cog(DeleteMsg(bot))