from Selection.selection import Selection
import random
import math
import numpy as np


class Boltzmann(Selection):
    def __init__(self, population_size, amount, tc, t0, k):
        super().__init__(population_size, amount)
        self.tc = tc
        self.t0 = t0
        self.k = k
        self.x = 0
        self.acc_functions = np.zeros(population_size)
        self.acc_performances = np.zeros(population_size)

    def select(self, population):
        population_size = self.population_size

        accumulated_functions = 0
        # Function is: e^(f(i)/Temperature)
        temp = self.tc + (self.t0 - self.tc)*math.exp(-self.k*self.x)
        self.x += 1
        for idx, character in enumerate(population):
            function_result = math.exp(character.get_performance() / temp)
            self.acc_functions[idx] = function_result
            accumulated_functions += function_result
        average_function = accumulated_functions/population_size

        for idx in range(population_size):
            self.acc_functions[idx] /= average_function
        total_func = sum(self.acc_functions)

        accumulated_performance = 0
        performances_dict = {}
        for idx, character in enumerate(population):
            accumulated_performance += (self.acc_functions[idx] / total_func)
            self.acc_performances[idx] = accumulated_performance
            performances_dict[accumulated_performance] = character
        self.acc_performances = np.sort(self.acc_performances)

        selected_population = []
        for _ in range(self.amount):
            rand = random.random()
            winner = np.searchsorted(self.acc_performances, rand)
            selected_population.append(performances_dict[self.acc_performances[winner]])

        return selected_population
