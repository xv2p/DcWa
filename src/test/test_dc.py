import discord
import asyncio

client = discord.Client(intents=discord.Intents.all())

message_queue = None

@client.event
async def on_ready():
    print("Bot Online")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message_queue.put(message.content)

async def setup():
    global message_queue
    message_queue = asyncio.Queue()
    await client.start("")