from SIA.TP2.Selection.selection import Selection
from SIA.TP2.sortedListAdapter import SortedListAdapter
import random
import math


class Ranking(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        k = self.amount
        population_size = len(population)

        # Ranking: Population ordered. At the end --> most performance char
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


        sorted_acc_rank_performance = sorted(acc_rank_performances.keys())
        random_numbers = {}
        for x in range(k):
            random_numbers[x] = random.randint(0, 1)

        selected_population = []
        for r_number in random_numbers:
            for acc_rank_performance in sorted_acc_rank_performance:
                if r_number > acc_rank_performance:
                    selected_population.append(acc_rank_performances[acc_rank_performance])
                    break

        return selected_population
