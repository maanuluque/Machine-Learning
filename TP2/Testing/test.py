import pandas as pd
import character
from Cross.annular import Annular
from Cross.one_point import OnePointCross
from Cross.two_point import TwoPointCross
from Cross.uniform import Uniform
from items import Items
from item import Item

#  Retrieve data for every type of item
print("Retrieving data from file....", end=' ')
weapons_data = pd.read_csv('../data/armas.tsv', sep="\t")
boots_data = pd.read_csv('../data/botas.tsv', sep="\t")
helmets_data = pd.read_csv('../data/cascos.tsv', sep="\t")
gloves_data = pd.read_csv('../data/guantes.tsv', sep="\t")
chests_data = pd.read_csv('../data/pecheras.tsv', sep="\t")
print("Done.")

# Set columns name
weapons_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
boots_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
helmets_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
gloves_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
chests_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]

# Size of each file
weapons_size = len(weapons_data.id)
boots_size = len(boots_data.id)
helmets_size = len(helmets_data.id)
gloves_size = len(gloves_data.id)
chests_size = len(chests_data.id)

# Testing Character methods
weapon = Item("weapon", weapons_data.id[0], weapons_data.strength[0],
              weapons_data.agility[0], weapons_data.expertise[0],
              weapons_data.resistance[0], weapons_data.health[0])

boots = Item("boots", boots_data.id[0], boots_data.strength[0],
             boots_data.agility[0], boots_data.expertise[0],
             boots_data.resistance[0], boots_data.health[0])

helmet = Item("helmet", helmets_data.id[0], helmets_data.strength[0],
              helmets_data.agility[0], helmets_data.expertise[0],
              helmets_data.resistance[0], helmets_data.health[0])

gloves = Item("gloves", gloves_data.id[0], gloves_data.strength[0],
              gloves_data.agility[0], gloves_data.expertise[0],
              gloves_data.resistance[0], gloves_data.health[0])

chest = Item("chest", chests_data.id[0], chests_data.strength[0],
             chests_data.agility[0], chests_data.expertise[0],
             chests_data.resistance[0], chests_data.health[0])

items1 = Items(weapon, boots, helmet, gloves, chest)

character1 = character.Defender(items1, 1.80)

weapon2 = Item("weapon", weapons_data.id[1], weapons_data.strength[1],
               weapons_data.agility[1], weapons_data.expertise[1],
               weapons_data.resistance[1], weapons_data.health[1])

boots2 = Item("boots", boots_data.id[1], boots_data.strength[1],
              boots_data.agility[1], boots_data.expertise[1],
              boots_data.resistance[1], boots_data.health[1])

helmet2 = Item("helmet", helmets_data.id[1], helmets_data.strength[1],
               helmets_data.agility[1], helmets_data.expertise[1],
               helmets_data.resistance[1], helmets_data.health[1])

gloves2 = Item("gloves", gloves_data.id[1], gloves_data.strength[1],
               gloves_data.agility[1], gloves_data.expertise[1],
               gloves_data.resistance[1], gloves_data.health[1])

chest2 = Item("chest", chests_data.id[1], chests_data.strength[1],
              chests_data.agility[1], chests_data.expertise[1],
              chests_data.resistance[1], chests_data.health[1])

items2 = Items(weapon2, boots2, helmet2, gloves2, chest2)

character2 = character.Defender(items2, 1.90)

character1.print_character()
character2.print_character()

character3 = character.Defender(items2, 1.70)
character4 = character.Defender(items1, 1.30)

character3.print_character()
character4.print_character()

cross = Uniform(2, 6, 0.5)
children = cross.cross([character1, character2])
print("\nchildren:\n")
for character in children:
    character.print_character()
"""
print("Height: " + str(character.height))

print("Attack Modifier: " + str(character.attack_modifier))
print("Defense Modifier: " + str(character.defense_modifier))

print("Items stats: " + str(character.items.stats))

print("Attack: " + str(character.attack))
print("Defense: " + str(character.defense))

print("Performance: " + str(character.performance))

"""
