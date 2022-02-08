from disnake.ext import commands
from disnake.ext.commands import *


class load_reload(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(f'cogs.normal-commands.{extension}')
            await ctx.send(f"{extension} 已上傳")
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f'cogs.normal-commands.{extension}')
            await ctx.send(f'{extension} 已卸載')
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        try:
            self.bot.reload_extension(f'cogs.normal-commands.{extension}')
            await ctx.send(f'{extension} 已更新')
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.add_cog(load_reload(bot))