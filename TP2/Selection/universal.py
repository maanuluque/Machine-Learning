from SIA.TP2.Selection.selection import Selection
import random


class Universal(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        total_performance = 0
        # TODO: Can be added when population is created
        for character in population:
            total_performance += character.performance

        accumulated_performance = 0
        acc_performances = {}  # Key: acc_performance (should be unique), Value --> Character
        for character in population:
            accumulated_performance += (character.performance / total_performance)
            character.accumulated_performance = accumulated_performance
            acc_performances[round(accumulated_performance, 3)] = character

        selected_population = []

        for index in range(self.amount):
            rand = round((round(random.random(), 2) + index) / self.amount, 3)
            for acc_performance in acc_performances.keys():
                if rand < acc_performance:
                    selected_population.append(acc_performances[acc_performance])
                    break

        return selected_population
