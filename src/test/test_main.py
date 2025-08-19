import discord
import test_dc
import asyncio

async def mess():
    while True:
        pesan = await test_dc.message_queue.get()
        print(pesan)

async def main():
    await asyncio.gather(test_dc.setup(),mess())

if __name__ == "__main__":
    asyncio.run(main())
