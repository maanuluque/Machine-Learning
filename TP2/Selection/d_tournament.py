from Selection.selection import Selection
import random


class DeterministicTournament(Selection):
    def __init__(self, population_size, amount, tournament_group_size):
        super().__init__(population_size, amount)
        self.tournament_group_size = tournament_group_size

    def select(self, population):
        population_size = len(population)

        if population_size < self.tournament_group_size:
            raise Exception('Tournament group size must be less than population size') from Exception

        index = 0
        selected_population = []
        temporal_tournament = []

        # while index < population_size:
        #     for x in range(self.tournament_group_size):
        #         if (index + x) < population_size:
        #             temporal_tournament.append(population[index + x])
        #         break
        #     index += self.tournament_group_size
        #     selected_population.append(temporal_tournament.pop())
        #     temporal_tournament.clear()

        for index in range(self.amount):
            for value in range(self.tournament_group_size):
                rand = random.randint(0,population_size-1)
                temporal_tournament.append(population[index])
            temporal_tournament.sort()
            selected_population.append(temporal_tournament.pop())
            temporal_tournament.clear()

        return selected_population

