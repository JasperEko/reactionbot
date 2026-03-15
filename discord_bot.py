import asyncio
import os
import discord
import requests

WEBHOOK = os.getenv("WEBHOOK", "https://hooks.zapier.com/hooks/catch/26815876/uxjlasi/")
TOKEN = os.getenv("TOKEN", "MTQ4MjU5MzY3MDIyNTA3MjMyMQ.GBaEAp._Cv1EF3yw9dEsgDEg98a7igV6uQME0uvg2zgSM")

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