import discord as ds
import os
from dotenv import load_dotenv

load_dotenv()

client = ds.Client()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.reply('hi', mention_author=True)

client.run(os.getenv('TOKEN'))
