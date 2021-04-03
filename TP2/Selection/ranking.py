from Selection.selection import Selection
import random
import math
import numpy as np

class Ranking(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)
        self.acc_rank_performances = np.zeros(population_size)

    def select(self, population):
        population_size = self.population_size

        # Ranking: Population ordered
        ranking = population.copy()
        ranking.sort()

        # Reverse iteration. Formula for Relative Rank Performance is:
        # F = [N - rank(i)] / N

        performances_dict = {}
        # Accumulated Rank Performance. Key: F, Value: Character
        for index in range(population_size):
            f = (population_size - index) / population_size # TODO index [0, N] or [1, N]?????
            self.acc_rank_performances[index] = f
            performances_dict[f] = ranking[index]
        self.acc_rank_performances = np.sort(self.acc_rank_performances)

 
        selected_population = []
        for index in range(self.amount):
            rand = random.random()
            winner = np.searchsorted(self.acc_rank_performances, rand)
            selected_population.append(performances_dict[self.acc_rank_performances[winner]])

        return selected_population
