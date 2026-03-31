import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ["commands","events","slash_commands"]:
            await self.load_extension(f"cogs.{extension}")


bot = MonBot(command_prefix="!",intents = discord.Intents.all())

bot.run(token = token)