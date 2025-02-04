import discord
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

# Event to notify when the bot has connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command /hi
@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')

# Run the bot with your token
bot.run('YOUR_DISCORD_BOT_TOKEN')
