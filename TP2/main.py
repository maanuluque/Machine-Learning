import json
import multiprocessing

import pandas as pd
from time import time, sleep

from boxplot import plot_diversity, plot_last_diversity
from graph import plot_gen
from items_diversity_graph import plot_items_div
from util import *

import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    algs = select_algorithms(config, population, items_db)
    print('Done.')

    # Start program
    print('Starting algorithm...')

    if config.last_diversity_graph:
        last_diversity = multiprocessing.Queue()
        process3 = multiprocessing.Process(target=plot_last_diversity, args=(last_diversity,))


    if config.live_graph:
        generations_list = multiprocessing.Queue()
        avg_fitness = multiprocessing.Queue()
        best_fitness = multiprocessing.Queue()

        process = multiprocessing.Process(target=plot_gen, args=(generations_list, best_fitness, avg_fitness))
        process.start()

    if config.diversity_graph:
        diversity_list = [[*map(map_performance, population)]]
        init_population = multiprocessing.Queue()
        nth_population = multiprocessing.Queue()
        last_population = multiprocessing.Queue()
        labels = multiprocessing.Queue()

        process2 = multiprocessing.Process(target=plot_diversity, args=(init_population, nth_population, last_population, labels))
        process2.start()

    if config.items_div_graph:
        shared_items_count = count_shared_items(population)
        shared_items_q = multiprocessing.Queue()
        generations_q = multiprocessing.Queue()

        shared_items_q.put(shared_items_count)
        generations_q.put(1)
        process4 = multiprocessing.Process(target=plot_items_div, args=(shared_items_q, generations_q))
        process4.start()


    generations = 1
    fmt = '{:<10} {}'
    cut_list = []
    parents_list = []
    cross_list = []
    mutate_list = []
    fill_list = []
    children_list = []
    newgen_list = []
    print_on = False
    init = time()
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

        if config.diversity_graph:
            diversity_list.append([*map(map_performance, population)])
            init_population.put(diversity_list[0])
            last_population.put(diversity_list[-1])
            mid = int(generations / 2)
            nth_population.put(diversity_list[mid-1])

            labels.put(("init", "mid", "last"))

        if config.live_graph:
            generations_list.put(generations)
            best_fitness.put(min(population).performance)
            avg_fitness.put(sum([i.performance for i in population]) / config.population_size)

        if config.items_div_graph:
            generations_q.put(generations)
            shared_items_q.put(count_shared_items(population))

    print(f'~ ~ ~ C O M P L E T E ~ ~ ~')

    if config.live_graph:
        while not best_fitness.empty():
            pass
        sleep(10)
        process.terminate()
    if config.diversity_graph:
        while not init_population.empty():
            pass
        sleep(10)
        process2.terminate()
    if config.last_diversity_graph:
        last_diversity.put([*map(map_performance, population)])
        process3.start()
        sleep(10)
        process3.terminate()
    if config.items_div_graph:
        while not shared_items_q.empty():
            pass
        sleep(10)
        process4.terminate()
    
    print('Time averages:')
    print(fmt.format('Cut: ', avg(cut_list)))
    print(fmt.format('Parents: ', avg(parents_list)))
    print(fmt.format('Cross: ', avg(cross_list)))
    print(fmt.format('Mutation: ', avg(mutate_list)))
    print(fmt.format('fill: ', avg(fill_list)))
    print(fmt.format('Children: ', avg(children_list)))
    print(fmt.format('NewGen: ', avg(newgen_list)))
    print()
    print(f'Execution Time: {round(time() - init, 3)}')
    print(f'Generations: {generations}')
    print(f'Population:  {len(population)}')
    print('Best character:')
    min(population).print_character()


if __name__ == "__main__":
    main()
