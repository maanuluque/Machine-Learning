import json
import pandas as pd
from time import time

from graph import plot_gen
from util import *

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

    print('Generating random initial population...')
    population = initial_population(config, items_db)
    print('Done.')
    print('Loading configuration...')
    algs = select_algorithms(config, population)
    print('Done.')

    # Start program
    print('Starting algorithm...')
    generations = 0
    generations_list = []
    avg_fitness = []
    best_fitness = []
    animation = None
    fmt = '{:<10} {}'
    cut_list = []
    parents_list = []
    cross_list = []
    mutate_list = []
    fill_list = []
    children_list = []
    newgen_list = []
    print_on = False
    while (True):
        print_on and print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # Cut
        t = time()
        finish = algs.cut.cut(population)
        d = time() - t
        cut_list.append(d)
        print_on and print(fmt.format('Cut:', d))
        if (finish):
            break

        # Select Parents
        t = time()
        selected_parents = algs.select_parents.select(population)
        d = time() - t
        parents_list.append(d)
        print_on and print(fmt.format('Parents:', d))

        # Crossover
        t = time()
        children = algs.crossover.cross(selected_parents)
        d = time() - t
        cross_list.append(d)
        print_on and print(fmt.format('Crossover:', d))

        # Mutation
        t = time()
        children = algs.mutation.mutate(children)
        d = time() - t
        mutate_list.append(d)
        print_on and print(fmt.format('Mutation:', d))

        # Fill
        t = time()
        new_generation = algs.fill.fill(population, children)
        d = time() - t
        fill_list.append(d)
        print_on and print(fmt.format('Fill:', d))

        # Select Children
        t = time()
        new_generation.extend(algs.select_children.select(population))
        d = time() - t
        children_list.append(d)
        print_on and print(fmt.format('Children:', d))

        # New Population
        t = time()
        population.clear()
        population.extend(new_generation)
        generations += 1
        d = time() - t
        newgen_list.append(d)
        print_on and print(fmt.format('Newpop:', d))

        generations_list.append(generations - 1)
        best_fitness.append(population[0].performance)
        avg_fitness.append(sum([i.performance for i in population]) / len(population))
        animation = plot_gen(generations_list, avg_fitness, best_fitness)
        # TODO graph

    print(f'~ ~ ~ C O M P L E T E ~ ~ ~')
    print('Time averages:')
    print(fmt.format('Cut: ', avg(cut_list)))
    print(fmt.format('Parents: ', avg(parents_list)))
    print(fmt.format('Cross: ', avg(cross_list)))
    print(fmt.format('Mutation: ', avg(mutate_list)))
    print(fmt.format('fill: ', avg(fill_list)))
    print(fmt.format('Children: ', avg(children_list)))
    print(fmt.format('NewGen: ', avg(newgen_list)))
    print()
    print(f'Generations: {generations}')
    print(f'Population:  {len(population)}')
    print('Best character:')
    population[0].print_character()


if __name__ == "__main__":
    main()
