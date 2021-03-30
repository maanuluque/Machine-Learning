from SIA.TP2.Selection.selection import Selection
import random
import math


class Boltzmann(Selection):
    def __init__(self, population_size, amount, temperature):
        super().__init__(population_size, amount)
        self.temperature = temperature

    def select(self, population):
        k = self.amount
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
            exp_values[character.exp_value/average_function] = character

        sorted_exp_values = sorted(exp_values.keys())

        random_numbers = {}
        for x in range(k):
            random_numbers[x] = random.randint(0, 1)

        selected_population = []
        for r_number in random_numbers:
            for exp_val in sorted_exp_values:
                if r_number > exp_val:
                    selected_population.append(exp_values[exp_val])
                    break

        return selected_population
