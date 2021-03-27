import json
import pandas as pd
import character
from types import SimpleNamespace as Obj
from items import Items
from item import Item
from Cut.time_cut import TimeCut

def initial_population(config, items):
    # TODO return array with initial random population
    # Initial heights must be uniformly dist [1.3 , 2.0] meters
    return [1, 2, 5, 8]

def select_algorithms(config, population):
    # TODO initialize classes (like TimeCut)
    algs = Obj()
    algs.cut = TimeCut(config.cut.time_limit)
    algs.cross = Obj()
    algs.cross.crossover = lambda x: x
    algs.mutation = Obj()
    algs.mutation.mutate = lambda x: x
    algs.fill = Obj()
    algs.fill.fill = lambda x: x
    algs.select_parents = Obj()
    algs.select_parents.select = lambda : [1, 2, 5, 8]
    algs.select_children = Obj()
    algs.select_children.select = lambda : [1, 2, 5, 8]

    return algs

def main():

    # Game config
    with open('config.json') as config_file:
        config = json.load(config_file, object_hook=lambda d: Obj(**d))

    print('Configuration:')
    print(f'Player class: {config.player_class}')
    print(f'Dataset: {config.dataset}')
    print(f'Population size: {config.population_size}')
    print(f'Fill: {config.fill}')
    print(f'Cross: {config.cross}')
    print(f'Mutation: {config.mutation}')
    print(f'Select parents: {config.select_parents}')
    print(f'Select children: {config.select_children}')
    print(f'Cut: {config.cut}')

    #  Retrieve data for every type of item
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

    population = initial_population(config, items_db)
    algs = select_algorithms(config, population)
    
    # Start program
    print('Starting..')
    while (not algs.cut.cut()):
        selected_parents = algs.select_parents.select()
        children = algs.cross.crossover(selected_parents)
        children = algs.mutation.mutate(children)
        new_generation = algs.fill.fill(children)
        new_generation.extend(algs.select_children.select())
    
        population.clear()
        population.extend(new_generation)

        # TODO graph

    print(f'Final population:')
    print(population)

if __name__ == "__main__":
    main()
