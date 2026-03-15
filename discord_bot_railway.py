import asyncio
import os
import discord
import requests
WEBHOOK = os.environ["WEBHOOK"]
TOKEN = os.environ["TOKEN"]
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.event
async def on_message(msg):
    if msg.author == client.user or "react" not in msg.content.lower():
        return
    asyncio.create_task(asyncio.to_thread(requests.post, WEBHOOK, json={"text": "react"}))
client.run(TOKEN)