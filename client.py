import os
from dotenv import load_dotenv
import discord

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
client = discord.Client(intents = discord.Intents.all())

client.run(token = token)