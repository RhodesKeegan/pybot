import discord as ds
import asyncio
from datetime import datetime
import os
from discord.ext import tasks, commands
from scraper import Scraper
from dotenv import load_dotenv

load_dotenv()
client = ds.Client()
scraper = Scraper()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')
    scrape.start()

@tasks.loop(seconds=1.0)
async def scrape():
    in_stock = scraper.check_availability()
    if 'add to cart' in in_stock.lower():
        channel = client.get_channel(921496506077438025)
        await channel.send(scraper.url)
        await asyncio.sleep(1800)

@scrape.before_loop
async def before_scrape():
    await client.wait_until_ready()

client.run(os.getenv('TOKEN'))
