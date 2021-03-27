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
    algs.cut = TimeCut(config.time_cut_limit)
    algs.cross = Obj()
    algs.cross.crossover = lambda x: x
    algs.mutation = Obj()
    algs.mutation.mutate = lambda x: x
    algs.select_parents = Obj()
    algs.select_parents.select = lambda x: x
    algs.select_children = Obj()
    algs.select_children.select = lambda x: x[:4]

    return algs

def main():

    # Game config
    with open('config.json') as config_file:
        data = json.load(config_file)

    config = Obj()
    config.player_class = data['player_class']
    config.cross = data['cross']
    config.mutation = data['mutation']
    config.select_parent_a = data['select_parent_a']
    config.select_parent_b = data['select_parent_b']
    config.select_child_a = data['select_child_a']
    config.select_child_b = data['select_child_b']
    config.percent_a = data['percent_a']
    config.percent_b = data['percent_b']
    config.fill = data['fill']
    config.cut = data['cut']
    config.dataset = data['dataset'] # TODO parametrizar dataset, solo 1 path a carpeta o path a cada uno??
    config.population_size = data['population_size']
    config.children_size = data['children_size']
    config.time_cut_limit = data['time_cut_limit']

    print('Configuration:')
    print(config.cross)
    print(config.mutation)
    print(config.select_parent_a)
    print(config.select_parent_b)
    print(config.select_child_a)
    print(config.select_child_b)
    print(config.percent_a)
    print(config.percent_b)
    print(config.fill)
    print(config.cut)
    print(config.dataset)

    #  Retrieve data for every type of item
    items_db = Obj()
    print("Retrieving data from file....")
    items_db.weapons_data = pd.read_csv('data/armas.tsv', sep="\t")
    items_db.boots_data = pd.read_csv('data/botas.tsv', sep="\t")
    items_db.helmets_data = pd.read_csv('data/cascos.tsv', sep="\t")
    items_db.gloves_data = pd.read_csv('data/guantes.tsv', sep="\t")
    items_db.chests_data = pd.read_csv('data/pecheras.tsv', sep="\t")
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
    only_children = config.children_size >= config.population_size
    new_generation = []
    print('starting..')
    while (not algs.cut.cut()):
        selected_parents = algs.select_parents.select(population)
        children = algs.cross.crossover(selected_parents)
        children = algs.mutation.mutate(children)

        new_generation.clear()
        if config.fill == 'fill_all': # Select from both parents and children 
            population.append(children)
        elif only_children: # Select only from children
            population.clear()
            population.extend(children)
        else: # Select only from parents (children already included)
            new_generation.extend(children)
        new_generation.extend(algs.select_children.select(population))

        population.clear()
        population.extend(new_generation)

        # TODO graph

    print(f'Final population:')
    print(population)

if __name__ == "__main__":
    main()
