from Selection.selection import Selection
import random

class ProbabilisticTournament(Selection):
    def __init__(self, population_size, amount, threshold):
        super().__init__(population_size, amount)
        self.threshold = threshold

    def select(self, population):
        population_size = self.population_size

        index = 0
        selected_population = []
        temporal_tournament = []

        for index in range(self.amount):
            for x in range(2):
                rand_character_index = random.randint(0, population_size-1)
                temporal_tournament.append(population[rand_character_index])
            temporal_tournament.sort()
            rand_r = random.random()
            if rand_r < self.threshold:
                selected_population.append(temporal_tournament.pop(0))
            else:
                selected_population.append(temporal_tournament.pop())
            temporal_tournament.clear()

        return selected_population
