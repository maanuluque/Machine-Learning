from Selection.selection import Selection
import random
import math
import numpy as np

class Ranking(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)
        self.acc_rank_performances = np.zeros(population_size)
        print(f'RANKING {amount}')

    def select(self, population):
        population_size = self.population_size

        # Ranking: Population ordered
        ranking = population.copy()
        ranking.sort()

        # Reverse iteration. Formula for Relative Rank Performance is:
        # F = [N - rank(i)] / N

        # Pseudo fitness
        for index in range(population_size):
            f = (population_size - (index+1)) / population_size
            self.acc_rank_performances[index] = f      

        total_fitness = sum(self.acc_rank_performances)
        accumulated_performance = 0
        performances_dict = {}
        for idx, character in enumerate(population):
            accumulated_performance += (self.acc_rank_performances[idx] / total_fitness)
            self.acc_rank_performances[idx] = accumulated_performance
            performances_dict[accumulated_performance] = character
        self.acc_rank_performances = np.sort(self.acc_rank_performances)

        selected_population = []
        for _ in range(self.amount):
            rand = random.random()
            winner = np.searchsorted(self.acc_rank_performances, rand)
            selected_population.append(performances_dict[self.acc_rank_performances[winner]])

        return selected_population
