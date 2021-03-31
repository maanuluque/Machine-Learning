from SIA.TP2.Selection.selection import Selection
from SIA.TP2.sortedListAdapter import SortedListAdapter
import random


class ProbabilisticTournament(Selection):
    def __init__(self, population_size, amount, threshold):
        super().__init__(population_size, amount)
        self.threshold = threshold

    def select(self, population):
        population_size = len(population)

        index = 0
        selected_population = []
        temporal_tournament = SortedListAdapter()
        # while index < population_size:
        #     for x in range(2):
        #         if (index + x) < population_size:
        #             temporal_tournament.append(population[index + x])
        #         break
        #     index += 2
        #     random_number = random.randint(0,1)
        #     if random_number < self.threshold:
        #         selected_population.append(temporal_tournament.pop())
        #     else:
        #         if selected_population:
        #             selected_population.append(temporal_tournament.pop(0))
        #     temporal_tournament.clear()

        for index in range(self.amount):
            for x in range(2):
                rand_character_index = random.randint(0, population_size-1)
                temporal_tournament.append(population[rand_character_index])
            rand_r = round(random.random(), 2)
            if rand_r < self.threshold:
                selected_population.append(temporal_tournament.pop())
            else:
                selected_population.append(temporal_tournament.pop(0))
            temporal_tournament.clear()

        return selected_population
