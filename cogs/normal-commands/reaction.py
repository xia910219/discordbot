from disnake.ext import commands
from disnake.ext.commands import *
import disnake

class Reaction(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: disnake.RawReactionActionEvent):
        if payload.message_id == 940572579343790120:
            if str(payload.emoji) == "🥒":
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(940495274550378507)
                await payload.member.add_roles(role)
                await payload.member.send(f"你取得了{role}身分組")
    
    #@commands.Cog.listener()
    #async def on_raw_reaction_remove(self, payload: disnake.RawReactionActionEvent):
    #    if payload.message_id == 940572579343790120:
    #        if str(payload.emoji) == "🥒":
    #            guild = self.get_guild(payload.guild_id) 
    #            print(1)
    #            user = await guild.fetch_user(payload.guild_id)
    #            role = guild.get_role(940495274550378507)
    #            member = guild.get_member(payload.user_id) 
    #            await member.remove_roles(role)
    #            await user.send(f"已移除{role}身分組")     


def setup(bot):
    bot.add_cog(Reaction(bot))