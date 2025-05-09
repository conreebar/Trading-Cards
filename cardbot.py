import os
import discord
from objects.Card import Card
from objects import CardUtils
from dao import userDAO, cardDAO, cardUserDAO
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Event to notify when the bot has connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name="general") 
        if channel:
            await channel.send('Hel lo, World!')
            break

    
# Command /hi
@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')

@bot.command()
async def showCard(ctx, *, card_name: str):
    card_data = cardDAO.getCardByName(card_name)
    if card_data:
        card = Card(**card_data)
        print(card)

        # Get the embed and the file from embedCard
        embed, file = card.embedCard()

        # Send the embed with the image if available
        if file:
            await ctx.send(embed=embed, file=file)
        else:
            await ctx.send(embed=embed)


@bot.command()
async def card(ctx):
    user_id = ctx.author.id
    username = ctx.author.name

    #check if user has a database object, if not add one
    user = userDAO.getUser(user_id)  # TODO make search func working with Discord user id
    if user:
        print(f"User already exists: {user}")
    else:
        print(f"User not found. Creating a new user...")
        userDAO.createUser(user_id)

    #TODO check if user has drawn a card in the past 24 hours

    #TODO roll 3 random cards and add to the account

    card_rarity = CardUtils.rollRarity() # make a rarity
    card_data = cardDAO.getRandomCardByRarity(card_rarity) #make a card from DAO
    

    # Convert the dictionary to a Card object
    if card_data:
        card = Card(**card_data)
        cardUserDAO.assignCardToUser(card.getCardID(), user_id) #assign card
        print(card)

        #embed card
        embed, file = card.embedCard()
        #Show card
        if file:
            await ctx.send(embed=embed, file=file)
        else:
            await ctx.send(embed=embed)
    

@bot.command()
async def showRandomCard(ctx):
    card_data = cardDAO.showRandomCard()
    # Convert the dictionary to a Card object
    if card_data:
        card = Card(**card_data)
        print(card)
        await ctx.send(embed=Card.embedCard(card))

@bot.command()
async def giveCardToUser(ctx, *, input_string: str):
    try:
        # Split input at the `|` character to separate user and card name
        user_mention, card_name = input_string.split(" | ")

        # Extract the user ID from the mention string by removing <@ and >
        user_id = int(user_mention[2:-1])

        # get card_id
        card_data = cardDAO.getCardByName(card_name.strip())  # Assuming a function to get card data
        
        if card_data:
            card_id = card_data['card_id']
            cardUserDAO.assignCardToUser(card_id, user_id)  # Assign the card to the user in the database
            await ctx.send(f"Card '{card_name.strip()}' has been successfully assigned to <@{user_id}>!")
        else:
            await ctx.send(f"No card found with the name '{card_name.strip()}'.")
    except ValueError:
        await ctx.send("Invalid input format. Please use `@username | card name`.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Run the bot with your token
discord_pass = os.getenv("DISSPASS")
bot.run(discord_pass)
