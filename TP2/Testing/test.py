import pandas as pd
import character
from Mutation.complete_mutation import CompleteMutation
from Mutation.gen_mutation import GenMutation
from Mutation.limited_multigen_mutation import LimitedMultigenMutation
from Mutation.uniform_multigen_mutation import UniformMultigenMutation
from items import Items
from item import Item
from types import SimpleNamespace as Obj

from main import rand_items

items_db = Obj()
#  Retrieve data for every type of item
print("Retrieving data from file....")
items_db.weapons_data = pd.read_csv(f'../data/armas.tsv', sep="\t")
items_db.boots_data = pd.read_csv(f'../data/botas.tsv', sep="\t")
items_db.helmets_data = pd.read_csv(f'../data/cascos.tsv', sep="\t")
items_db.gloves_data = pd.read_csv(f'../data/guantes.tsv', sep="\t")
items_db.chests_data = pd.read_csv(f'../data/pecheras.tsv', sep="\t")
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

items1 = rand_items(items_db)
items2 = rand_items(items_db)

character1 = character.Defender(items1, 1.90)
character2 = character.Defender(items2, 1.90)

character1.print_character()
character2.print_character()

mutation = CompleteMutation(2, 0.5, 1.30, 2.00, items_db)
children = mutation.mutate([character1, character2])
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

print("Performance: " + str(character.get_performance()))

"""
