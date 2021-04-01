from Selection.selection import Selection
import random
import math


class Boltzmann(Selection):
    def __init__(self, population_size, amount, temperature):
        super().__init__(population_size, amount)
        self.temperature = temperature

    def select(self, population):
        population_size = len(population)

        accumulated_functions = 0
        # Function is: e^(f(i)/Temperature)
        for character in population:
            function_result = math.exp(character.performance/self.temperature)
            character.exp_value = function_result
            accumulated_functions += function_result

        average_function = accumulated_functions/population_size

        exp_values = {}

        for character in population:
            value = round(character.exp_value/average_function, 3)
            exp_values[value] = character

        for key in exp_values.keys():
            print(str(key), end=' ')
        print()

        selected_population = []

        # TODO: Improve random float, or improve average function
        # exp_values sometimes greater than 1 :(
        for index in range(self.amount):
            rand = round(random.random(), 3)
            for exp_val in exp_values.keys():
                if rand < exp_val:
                    selected_population.append(exp_values[exp_val])
                    break

        return selected_population
