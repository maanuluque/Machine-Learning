from Selection.selection import Selection
import random
import numpy as np

class Roulette(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)
        self.acc_performances = np.zeros(population_size)
        print(f'ROULETTE {amount}')

    def select(self, population):
        total_performance = 0
        # TODO: Can be added when population is created
        for character in population:
            total_performance += character.get_performance()

        accumulated_performance = 0
        performances_dict = {} # Key: acc_performance (should be unique), Value --> Character
         
        for idx, character in enumerate(population):
            accumulated_performance += (character.get_performance() / total_performance)
            self.acc_performances[idx] = accumulated_performance
            performances_dict[accumulated_performance] = character
        self.acc_performances = np.sort(self.acc_performances)

        selected_population = []
        for _ in range(self.amount):
            rand = random.random()
            winner = np.searchsorted(self.acc_performances, rand)
            selected_population.append(performances_dict[self.acc_performances[winner]])

        return selected_population
