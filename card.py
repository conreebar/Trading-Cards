import os
import discord
from discord.ext import commands

# Set up the bot with a command prefix
#intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='/', intents=intents)

# Event to notify when the bot has connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command /hi
@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')

@bot.command()
async def openCard(ctx):
    await ctx.send('in progress')

# Run the bot with your token
discord_pass = os.getenv("DISSPASS")
bot.run(discord_pass)
