import random
import json
import pandas as pd
import character
from time import time
from types import SimpleNamespace as Obj
from sortedListAdapter import SortedListAdapter
from items import Items
from item import Item
from Cut import *
from Cross import *
from Mutation import *
from Fill import *
from Selection import *


def rand_items(items_db):
    weapon = rand_weapon(items_db)
    boots = rand_boots(items_db)
    helmet = rand_helmet(items_db)
    gloves = rand_gloves(items_db)
    chest = rand_chest(items_db)
    items = Items(weapon, boots, helmet, gloves, chest)
    return items


def rand_height(max_h, min_h):
    return random.uniform(max_h, min_h)  # TODO round decimals?


def rand_weapon(items_db):
    weapon_id = random.randint(0, items_db.weapons_size - 1)
    weapon = Item("weapon", items_db.weapons_data.id[weapon_id], items_db.weapons_data.strength[weapon_id],
                  items_db.weapons_data.agility[weapon_id], items_db.weapons_data.expertise[weapon_id],
                  items_db.weapons_data.resistance[weapon_id], items_db.weapons_data.health[weapon_id])
    return weapon


def rand_boots(items_db):
    boots_id = random.randint(0, items_db.boots_size - 1)
    boots = Item("boot", items_db.boots_data.id[boots_id], items_db.boots_data.strength[boots_id],
                 items_db.boots_data.agility[boots_id], items_db.boots_data.expertise[boots_id],
                 items_db.boots_data.resistance[boots_id], items_db.boots_data.health[boots_id])
    return boots


def rand_helmet(items_db):
    helmet_id = random.randint(0, items_db.helmets_size - 1)
    helmet = Item("helmet", items_db.helmets_data.id[helmet_id], items_db.helmets_data.strength[helmet_id],
                  items_db.helmets_data.agility[helmet_id], items_db.helmets_data.expertise[helmet_id],
                  items_db.helmets_data.resistance[helmet_id], items_db.helmets_data.health[helmet_id])
    return helmet


def rand_gloves(items_db):
    gloves_id = random.randint(0, items_db.gloves_size - 1)
    gloves = Item("gloves", items_db.gloves_data.id[gloves_id], items_db.gloves_data.strength[gloves_id],
                  items_db.gloves_data.agility[gloves_id], items_db.gloves_data.expertise[gloves_id],
                  items_db.gloves_data.resistance[gloves_id], items_db.gloves_data.health[gloves_id])
    return gloves


def rand_chest(items_db):
    chest_id = random.randint(0, items_db.chests_size - 1)
    chest = Item("chest", items_db.chests_data.id[chest_id], items_db.chests_data.strength[chest_id],
                 items_db.chests_data.agility[chest_id], items_db.chests_data.expertise[chest_id],
                 items_db.chests_data.resistance[chest_id], items_db.chests_data.health[chest_id])
    return chest


def initial_population(config, items_db):
    times = config.population_size
    max_h = config.max_height
    min_h = config.min_height
    useSort = (config.select_parents.method_1 == 'elite' or
               config.select_parents.method_2 == 'elite' or
               config.select_parents.method_1 == 'ranking' or
               config.select_parents.method_2 == 'ranking' or
               config.select_children.method_1 == 'elite' or
               config.select_children.method_2 == 'elite' or
               config.select_children.method_1 == 'ranking' or
               config.select_children.method_2 == 'ranking' or
               config.cut.method == 'acceptable' or
               config.cut.method == 'structure_cut')

    print(f'Sorted population list: {useSort}')
    population = SortedListAdapter() if useSort else []
    # population = SortedListAdapter()
    # population = []
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

    while times > 0:
        items = rand_items(items_db)
        height = random.uniform(max_h, min_h)  # TODO round decimals?
        char = character_class(items, height)
        population.append(char)
        times -= 1

    return population


def select_algorithms(config, population):
    algs = Obj()
    pop_size = config.population_size
    parents_size = config.select_parents.amount
    children_size = parents_size
    item_keys = list(population[0].items.equipment)

    # Cut
    if config.cut.method == 'acceptable_cut':
        algs.cut = AcceptableCut(config.cut.acceptable_fitness)
    elif config.cut.method == 'generations_cut':
        algs.cut = GenerationsCut(config.cut.generations_limit)
    elif config.cut.method == 'structure_cut':
         algs.cut = StructureCut(round(pop_size*config.cut.structure_percent), config.cut.generations_limit, population, config.cut.fitness_decimals)
    else:
        algs.cut = TimeCut(config.cut.time_limit)

    # Cross
    if config.cross.method == 'one_point':
        algs.crossover = OnePointCross(children_size, config.genome_size, item_keys)
    elif config.cross.method == 'two_point':
        algs.crossover = TwoPointCross(children_size, config.genome_size, item_keys)
    elif config.cross.method == 'annular':
        algs.crossover = Annular(children_size, config.genome_size, item_keys)
    elif config.cross.method == 'uniform':
        algs.crossover = Uniform(children_size, config.genome_size, item_keys, config.cross.uniform_prob)
    else:
        print('Default to no-crossover')
        algs.crossover = NoCross(children_size, config.genome_size, item_keys)

    # Mutation
    if config.mutation.method == 'no_mutation':
        algs.mutation = NoMutation(children_size, config.mutation.probability)

    # Select Parents
    A1 = round(parents_size * config.select_parents.percent_1)
    A2 = parents_size - A1
    threshold = config.select_parents.tournament_threshold
    tournament_group = config.select_parents.tournament_group
    temperature = config.select_parents.boltzmann_temp

    if config.select_parents.method_1 == 'select_all':
        sp_1 = SelectAll(pop_size, A1)
    elif config.select_parents.method_1 == 'roulette':
        sp_1 = Roulette(pop_size, A1)
    elif config.select_parents.method_1 == 'elite':
        sp_1 = Elite(pop_size, A1)
    elif config.select_parents.method_1 == 'universal':
        sp_1 = Universal(pop_size, A1)
    elif config.select_parents.method_1 == 'ranking':
        sp_1 = Ranking(pop_size, A1)
    elif config.select_parents.method_1 == 'd_tournament':
        sp_1 = DeterministicTournament(pop_size, A1, tournament_group)
    elif config.select_parents.method_1 == 'p_tournament':
        sp_1 = ProbabilisticTournament(pop_size, A1, threshold)
    elif config.select_parents.method_1 == 'boltzmann':
        sp_1 = Boltzmann(pop_size, A1, temperature)
    else:
        raise Exception('Invalid selection method. ') from Exception

    if config.select_parents.method_2 == 'select_all':
        sp_2 = SelectAll(pop_size, A2)
    elif config.select_parents.method_2 == 'roulette':
        sp_2 = Roulette(pop_size, A2)
    elif config.select_parents.method_2 == 'elite':
        sp_2 = Elite(pop_size, A2)
    elif config.select_parents.method_2 == 'universal':
        sp_2 = Universal(pop_size, A2)
    elif config.select_parents.method_2 == 'ranking':
        sp_2 = Ranking(pop_size, A2)
    elif config.select_parents.method_2 == 'd_tournament':
        sp_2 = DeterministicTournament(pop_size, A2, tournament_group)
    elif config.select_parents.method_2 == 'p_tournament':
        sp_2 = ProbabilisticTournament(pop_size, A2, threshold)
    elif config.select_parents.method_2 == 'boltzmann':
        sp_2 = Boltzmann(pop_size, A2, temperature)
    else:
        raise Exception('Invalid selection method. ') from Exception

    algs.select_parents = DoubleSelection(sp_1, sp_2)

    # Select Children
    if config.fill == 'fill_all':
        old_gen_size = pop_size + children_size
        new_gen_size = pop_size
    elif pop_size <= children_size:
        old_gen_size = children_size
        new_gen_size = pop_size
    else:
        old_gen_size = parents_size
        new_gen_size = pop_size - children_size
    B1 = round(new_gen_size * config.select_children.percent_1)
    B2 = new_gen_size - B1
    threshold_children = config.select_children.tournament_threshold
    tournament_group_children = config.select_children.tournament_group
    temperature_children = config.select_children.boltzmann_temp
    
    if config.select_children.method_1 == 'select_all':
        sc_1 = SelectAll(old_gen_size, B1)
    if config.select_children.method_1 == 'roulette':
        sc_1 = Roulette(old_gen_size, B1)
    if config.select_children.method_1 == 'elite':
        sc_1 = Elite(old_gen_size, B1)
    if config.select_children.method_1 == 'universal':
        sc_1 = Universal(old_gen_size, B1)
    if config.select_children.method_1 == 'ranking':
        sc_1 = Ranking(old_gen_size, B1)
    if config.select_children.method_1 == 'd_tournament':
        sc_1 = DeterministicTournament(old_gen_size, B1, tournament_group_children)
    if config.select_children.method_1 == 'p_tournament':
        sc_1 = ProbabilisticTournament(old_gen_size, B1, threshold_children)
    if config.select_children.method_1 == 'boltzmann':
        sc_1 = Boltzmann(old_gen_size, B1, temperature_children)
        
    if config.select_children.method_2 == 'select_all':
        sc_2 = SelectAll(old_gen_size, B2)
    if config.select_children.method_1 == 'roulette':
        sc_2 = Roulette(old_gen_size, B2)
    if config.select_children.method_1 == 'elite':
        sc_2 = Elite(old_gen_size, B2)
    if config.select_children.method_1 == 'universal':
        sc_2 = Universal(old_gen_size, B2)
    if config.select_children.method_1 == 'ranking':
        sc_2 = Ranking(old_gen_size, B2)
    if config.select_children.method_1 == 'd_tournament':
        sc_2 = DeterministicTournament(old_gen_size, B2, tournament_group_children)
    if config.select_children.method_1 == 'p_tournament':
        sc_2 = ProbabilisticTournament(old_gen_size, B2, threshold_children)
    if config.select_children.method_1 == 'boltzmann':
        sc_2 = Boltzmann(old_gen_size, B2, temperature_children)

    algs.select_children = DoubleSelection(sc_1, sc_2)

    # Fill Implementation
    if config.fill == 'fill_all':
        algs.fill = FillAll(pop_size, children_size)

    return algs


def print_pop(population):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for p in population:
        p.print_character()

def avg(l: list):
    size = len(l)
    total = sum(l)
    return round(total/size, 6)


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
