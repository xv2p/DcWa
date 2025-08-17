import discord
from discord.ext import commands
class Disc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bridge from DC")
        channel = self.bot.get_channel(959667506795118645)
        await channel.send("online")
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        print(f"{message.author} : {message.content}")

    
async def setup(bot):
    await bot.add_cog(Disc(bot))
