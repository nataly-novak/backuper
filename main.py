import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='copy', help="backups current channel")
async def copy(ctx):
    f = open(ctx.channel.name+".txt", "w")
    async for message in ctx.channel.history(limit=None, oldest_first=True):
        f.write(str(message.author.name) +": " + message.content+"\n")
    await ctx.send("done")
bot.run(TOKEN)