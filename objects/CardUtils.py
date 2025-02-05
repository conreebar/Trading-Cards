import random
#Card rarity: subject to change
    #55% common 
    #30% uncommon
    #10% rare
    #4% epic
    #1% legendary
def rollRarity():
    rand_Int = random.randint(1, 100)
    card_rarity = 0
    if rand_Int == 1:
        card_rarity = 'Legendary'
    elif rand_Int <= 5:
        card_rarity = 'Epic'
    elif rand_Int <= 15:
        card_rarity = 'Rare'
    elif rand_Int <= 45:
        card_rarity = 'Uncommon'
    elif rand_Int <= 100:
        card_rarity = 'Common'
    return card_rarity