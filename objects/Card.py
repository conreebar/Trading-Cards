import os
import discord
from dao import cardDAO


class Card:
    def __init__(self, card_id, card_name, rarity, flavor_text, card_set, image_loc):
        self.card_id = card_id
        self.card_name = card_name
        self.rarity = rarity
        self.flavor_text = flavor_text
        self.card_set = card_set
        self.image_loc = image_loc

    def __str__(self):
        return f"{self.card_name} ({self.rarity}): {self.flavor_text}"
    
    def getCardID(self):
        return self.card_id

    

    def rarityColor(self):
        if self.rarity == 'Common':
            return discord.Color.green()
        elif self.rarity == 'Uncommon':
            return discord.Color.blue()
        elif self.rarity == 'Rare':
            return discord.Color.purple()
        elif self.rarity == 'Epic':
            return discord.Color.red() 
        elif self.rarity == 'Legendary':
            return discord.Color.gold()
        else:
            return discord.Color.default()

    def embedCard(self):
        card_color = self.rarityColor()
        embed = discord.Embed(
            title=self.card_name,
            description=self.flavor_text,
            color=card_color,
        )

        # Extract the image name from image_loc
        if hasattr(self, 'image_loc') and self.image_loc:
            image_name = os.path.basename(self.image_loc)  # e.g., "imageName.png"
            file = discord.File(self.image_loc, filename=image_name)
            embed.set_image(url=f"attachment://{image_name}")
            return embed, file
        else:
            return embed, None

        return(embed)



        