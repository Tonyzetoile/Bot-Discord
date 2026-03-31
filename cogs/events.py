import discord
from discord.ext import commands
import asyncio
import sqlite3
import time

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connexion = sqlite3.connect("warnings.db")
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS warnings
                          (user_id INTEGER PRIMARY KEY, warnings INTEGER,warning_time REAL);''')
        self.connexion.commit()
        self.user_messages = {}

    @commands.Cog.listener("on_message")
    async def user_warning(self, message: discord.Message):
        user_id = message.author.id
        current_time = time.time()

        """print(f"id du bot : {self.bot.user.id}")
        print(f"id de l'user : {user_id}")"""
        if user_id == self.bot.user.id:
            return

        if user_id not in self.user_messages:
            self.user_messages[user_id] = []
        self.user_messages[user_id].append(current_time)

        self.user_messages[user_id] = [timestamp for timestamp in self.user_messages[user_id] if current_time - timestamp <= 10]

        if len(self.user_messages[user_id]) > 10:
            await message.channel.send(f"{message.author.mention}\nAvertissement : tu envoies des messages trop rapidement. Merci de ralentir.")
            self.cursor.execute("SELECT warnings FROM warnings WHERE user_id = ?", (user_id,), ";")
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute("UPDATE warnings SET warnings = warnings + 1, warning_time= ? WHERE user_id = ?", (user_id,), ";")
            else:
                self.cursor.execute("INSERT INTO warnings (user_id, warnings,warning_time) VALUES (?, 1,?)", (user_id,), ";")
            self.connexion.commit()
            self.user_messages[user_id].clear()
            return

        await asyncio.sleep(1)

    async def close_db(self):
        self.connexion.commit()
        self.connexion.close()

async def setup(bot):
    await bot.add_cog(EventsCog(bot))