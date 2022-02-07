from disnake.ext import commands
import random

class Earn(commands.Cog):
    #def __init__(self, bot):
    #    self.bot = bot
    
    @commands.command(pass_context = True)
    async def earn(self, ctx):
        money = random.randint(0, 5)
        await ctx.send(f"money :  {money} is comming ~")

def setup(bot):
    bot.add_cog(Earn(bot))