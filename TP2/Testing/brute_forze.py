import json
import pandas as pd
from types import SimpleNamespace as Obj
from time import time
import character
from items import *
import decimal
from numpy import arange

#  Retrieve data for every type of item
with open('config.json') as config_file:
    config = json.load(config_file, object_hook=lambda d: Obj(**d))

items_db = Obj()
print("Retrieving data from file....")
items_db.weapons_data = pd.read_csv(f'{config.dataset}/armas.tsv', sep="\t")
items_db.boots_data = pd.read_csv(f'{config.dataset}/botas.tsv', sep="\t")
items_db.helmets_data = pd.read_csv(f'{config.dataset}/cascos.tsv', sep="\t")
items_db.gloves_data = pd.read_csv(f'{config.dataset}/guantes.tsv', sep="\t")
items_db.chests_data = pd.read_csv(f'{config.dataset}/pecheras.tsv', sep="\t")
print("Done.")

# Set columns name
items_db.weapons_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
items_db.boots_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
items_db.helmets_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
items_db.gloves_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]
items_db.chests_data.columns = ["id", "strength", "agility", "expertise", "resistance", "health"]

# Size of each file
items_db.weapons_size = len(items_db.weapons_data.id)
items_db.boots_size = len(items_db.boots_data.id)
items_db.helmets_size = len(items_db.helmets_data.id)
items_db.gloves_size = len(items_db.gloves_data.id)
items_db.chests_size = len(items_db.chests_data.id)

max_h = config.max_height
min_h = config.min_height
delta_h = config.delta_h

if config.player_class == 'warrior':
    character_class = character.Warrior
elif config.player_class == 'archer':
    character_class = character.Archer
elif config.player_class == 'defender':
    character_class = character.Defender
elif config.player_class == 'infiltrate':
    character_class = character.Infiltrate
else:
    raise Exception('Invalid player class') from Exception

def create_char(clazz, height, weapon_id, boots_id, helmet_id, gloves_id, chest_id):
    weapon = Item("weapon", items_db.weapons_data.id[weapon_id], items_db.weapons_data.strength[weapon_id],
                  items_db.weapons_data.agility[weapon_id], items_db.weapons_data.expertise[weapon_id],
                  items_db.weapons_data.resistance[weapon_id], items_db.weapons_data.health[weapon_id])
    boots = Item("boot", items_db.boots_data.id[boots_id], items_db.boots_data.strength[boots_id],
                 items_db.boots_data.agility[boots_id], items_db.boots_data.expertise[boots_id],
                 items_db.boots_data.resistance[boots_id], items_db.boots_data.health[boots_id])
    helmet = Item("helmet", items_db.helmets_data.id[helmet_id], items_db.helmets_data.strength[helmet_id],
                  items_db.helmets_data.agility[helmet_id], items_db.helmets_data.expertise[helmet_id],
                  items_db.helmets_data.resistance[helmet_id], items_db.helmets_data.health[helmet_id])
    gloves = Item("gloves", items_db.gloves_data.id[gloves_id], items_db.gloves_data.strength[gloves_id],
                  items_db.gloves_data.agility[gloves_id], items_db.gloves_data.expertise[gloves_id],
                  items_db.gloves_data.resistance[gloves_id], items_db.gloves_data.health[gloves_id])
    chest = Item("chest", items_db.chests_data.id[chest_id], items_db.chests_data.strength[chest_id],
                 items_db.chests_data.agility[chest_id], items_db.chests_data.expertise[chest_id],
                 items_db.chests_data.resistance[chest_id], items_db.chests_data.health[chest_id])
    items = Items(weapon, boots, helmet, gloves, chest)
    return clazz(items, height)


best = create_char(character_class, min_h, 0, 0, 0, 0, 0)
height_list = list(arange(min_h, max_h+delta_h, delta_h))

for w in range(0, items_db.weapons_size):
    print('next weapon..')
    for b in range(0, items_db.boots_size):
        print('  next boot..')
        for hm in range(0, items_db.helmets_size):
            print('    next helmet..')
            for g in range(0, items_db.gloves_size):
                for c in range(0, items_db.chests_size):
                    for ht in height_list:
                        char = create_char(character_class, ht, w, b, hm, g, c)
                        if char.get_performance() > best.get_performance():
                            best = char
        print(f'Current best: {best.get_performance()}')

best.print_character()
