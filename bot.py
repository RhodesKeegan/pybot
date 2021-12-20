import discord as ds
import os
from scraper import Scraper
from dotenv import load_dotenv

load_dotenv()

client = ds.Client()

scraper = Scraper()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower()

    if f'$search' in content:
        key_words, search_words = scraper.keywords_search_words(content)
        result_links = scraper.search(key_words)
        links = scraper.send_link(result_links, search_words)
        if len(links) > 0:
            for link in links:
                await message.channel.send(link)
        else:
            await message.channel.send('No results found :(')

client.run(os.getenv('TOKEN'))
