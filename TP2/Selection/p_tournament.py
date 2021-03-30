from SIA.TP2.Selection.selection import Selection
from SIA.TP2.sortedListAdapter import SortedListAdapter
import random


class deterministicTournament(Selection):
    def __init__(self, population_size, amount, threeshold):
        super().__init__(population_size, amount)
        self.threeshold = threeshold

    def select(self, population):
        population_size = len(population)

        index = 0
        selected_population = []
        temporal_tournament = SortedListAdapter()
        while index < population_size:
            for x in range(2):
                if (index + x) < population_size:
                    temporal_tournament.append(population[index + x])
                break
            index += 2
            random_number = random.randint(0,1)
            if random_number < self.threeshold:
                selected_population.append(temporal_tournament.pop())
            else:
                selected_population.append(temporal_tournament.pop(1))
            temporal_tournament.clear()

        return selected_population
