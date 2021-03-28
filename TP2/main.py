import json
import pandas as pd
import character
from types import SimpleNamespace as Obj
from items import Items
from item import Item
from Cut.time_cut import TimeCut
from Cut.generations_cut import GenerationsCut
from Fill.fill_all import FillAll
from Mutation.no_mutation import NoMutation
from Selection.double_selection import DoubleSelection
from Selection.select_all import SelectAll
from Cross.no_cross import NoCross


def initial_population(config, items):
    # TODO return array with initial random population
    # Initial heights must be uniformly dist [1.3 , 2.0] meters
    return [1, 2, 5, 8, 3, 0, 4, 7, 6, 9]

def select_algorithms(config, population):
    # TODO initialize classes (like TimeCut)
    algs = Obj()
    population_amount = config.population_size

    # Cut
    if config.cut.method == 'time_cut':
        algs.cut = TimeCut(config.cut.time_limit)
    elif config.cut.method == 'generations_cut':
        algs.cut = GenerationsCut(config.cut.generations_limit)

    # Cross
    if config.cross.method == 'no_cross':
        algs.crossover = NoCross(config.genome_size)

    # Mutation
    if config.mutation.method == 'no_mutation':
        algs.mutation = NoMutation(config.mutation.probability)

    # Select Parents
    parents_amount = config.select_parents.amount
    A1 = round(parents_amount*config.select_parents.percent_1)
    A2 = parents_amount - A1
    if config.select_parents.method_1 == 'select_all':
        sp_1 = SelectAll(population_amount, A1)
    if config.select_parents.method_2 == 'select_all':
        sp_2 = SelectAll(population_amount, A2)
    algs.select_parents = DoubleSelection(sp_1, sp_2)

    # Select Children
    children_amount = config.select_children.amount
    B1 = round(children_amount*config.select_children.percent_1)
    B2 = children_amount - B1
    if config.select_children.method_1 == 'select_all':
        sc_1 = SelectAll(population_amount, B1)
    if config.select_children.method_2 == 'select_all':
        sc_2 = SelectAll(population_amount, B1)
    algs.select_children = DoubleSelection(sc_1, sc_2)

    # Fill Implementation
    if config.fill == 'fill_all':
        algs.fill = FillAll(population_amount, children_amount)

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
    while (not algs.cut.cut(population)):
        selected_parents = algs.select_parents.select(population)
        children = algs.crossover.cross(selected_parents)
        children = algs.mutation.mutate(children)
        population, new_generation = algs.fill.fill(population, children)
        new_generation.extend(algs.select_children.select(population))
    
        population = new_generation

        # TODO graph

    print(f'Final population:')
    print(population)

if __name__ == "__main__":
    main()
