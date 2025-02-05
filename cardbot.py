import os
import discord
from objects.Card import Card
from dao import userDAO, cardDAO
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

    # Get the channel by name
    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name="general")  # Replace 'general' with your channel name
        if channel:
            await channel.send('Hello, World!')
            break
    # Sync commands
    try:
        # Sync the slash commands to Discord's servers
        await bot.tree.sync()  # This syncs the commands globally
        print('Slash commands synchronized successfully.')
    except Exception as e:
        print(f'Error syncing commands: {e}')

    
# Command /hi
@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')

@bot.command()
async def showCard(ctx, *,card_name:str):
    card_data = cardDAO.getCardByName(card_name)
    if card_data:
        card = Card(**card_data)
        print(card)
        await ctx.send(embed=Card.embedCard(card))

@bot.command()
async def card(ctx):
    user_id = ctx.author.id # grab user_id from user who submitted the command
    username = ctx.author.name

    #check if user has a database object, if not add one
    user = userDAO.getUser(user_id)  # TODO make search func working with Discord user id
    if user:
        print(f"User already exists: {user}")
    else:
        print(f"User not found. Creating a new user...")
        userDAO.createUser(user_id)  # Create the user if not found
    #check if user has drawn a card in the past 24 hours

    #roll a random card and add to the account

    await ctx.send(f'{user_id} and {username}')

@bot.command()
async def showRandomCard(ctx):
    card_data = cardDAO.showRandomCard()
    # Convert the dictionary to a Card object
    if card_data:
        card = Card(**card_data)
        print(card)
        await ctx.send(embed=Card.embedCard(card))
    

# Run the bot with your token
discord_pass = os.getenv("DISSPASS")
bot.run(discord_pass)
