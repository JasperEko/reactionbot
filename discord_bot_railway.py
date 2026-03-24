import os
import discord
from discord.ext import commands
import random

# Create bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Your phrases and images
items = [
  "Hey emo boy. Hey hey hey emo boy",
  "DAVID BASZUCKI...",
  "yall think disneys chicken little is a 10/10 game",
  "i wish i was high on potenuse",
  "bro lookin like an ipad kid 💀💀💀💀💀☠️☠️☠️",
  "im spongebob im spongebob",
  "i do that too",
  "a wacky spin on a popular classic!",
  "charlie kirk in mha: here's my charlie quirk",
  "DELTARUNE BACKWARDS IS UNDERTALE",
  "mmm yummy slop",
  "https://image2url.com/r2/default/images/1773561788341-c382783b-170f-4e15-b3dd-496b010aaf26.png",
  "https://image2url.com/r2/default/images/1773894962347-e2b7a674-9471-4d37-bffb-2b941f290815.jpg",
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "react":
        random_item = random.choice(items)

        if random_item.startswith("http"):
            await message.channel.send(embed=discord.Embed().set_image(url=random_item))
        else:
            await message.channel.send(random_item)

bot.run(os.environ["TOKEN"])
