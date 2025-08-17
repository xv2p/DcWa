import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

Token = os.getenv("Token")



bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

async def setup_hook():
    await bot.load_extension("dc")


if __name__ == "__main__":
    bot.setup_hook = setup_hook
    bot.run(Token)