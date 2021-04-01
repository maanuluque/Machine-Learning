from Selection.selection import Selection
from sortedListAdapter import SortedListAdapter
import random
import math


class Ranking(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        population_size = len(population)

        # Ranking: Population ordered. At the end --> most performance character
        ranking = SortedListAdapter()
        for x in range(population_size):
            ranking.append(population[x])

        # Reverse iteration. Formula for Relative Rank Performance is:
        # F = [N - rank(i)] / N

        acc_rank_performances = {}
        # Accumulated Rank Performance. Key: F, Value: Character
        for index in range(population_size):
            f = (population_size - (population_size - 1 - index)) / population_size
            acc_rank_performances[f] = ranking[index]

        selected_population = []
        for index in range(self.amount):
            rand = round(random.random(), 2)
            for acc_rank_performance in acc_rank_performances.keys():
                if rand < acc_rank_performance:
                    selected_population.append(acc_rank_performances[acc_rank_performance])
                    break

        return selected_population
