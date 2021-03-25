import pandas as pd
import character
from items import Items
from item import Item

#  Retrieve data for every type of item
weapons_data = pd.read_csv('data/armas.tsv', sep="\t")
boots_data = pd.read_csv('data/botas.tsv', sep="\t")
helmets_data = pd.read_csv('data/cascos.tsv', sep="\t")
gloves_data = pd.read_csv('data/guantes.tsv', sep="\t")
chests_data = pd.read_csv('data/pecheras.tsv', sep="\t")

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

warrior = character.Warrior(items1, 1.80)
print("Height: " + str(warrior.height))

print("Attack Modifier: " + str(warrior.attack_modifier))
print("Defense Modifier: " + str(warrior.defense_modifier))

print("Items stats: " + str(warrior.items.stats))

print("Attack: " + str(warrior.attack))
print("Defense: " + str(warrior.defense))

print("Performance: " + str(warrior.performance))
