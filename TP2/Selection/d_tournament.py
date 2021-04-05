from Selection.selection import Selection
import random


class DeterministicTournament(Selection):
    def __init__(self, population_size, amount, tournament_group_size):
        super().__init__(population_size, amount)
        self.tournament_group_size = tournament_group_size
        print(f'DTOUR: {self.amount}')

    def select(self, population):
        population_size = self.population_size

        if population_size < self.tournament_group_size:
            raise Exception('Tournament group size must be less than population size') from Exception

        index = 0
        selected_population = []
        temporal_tournament = []

        for index in range(self.amount):
            for value in range(self.tournament_group_size):
                rand = random.randint(0,population_size-1)
                temporal_tournament.append(population[rand])
            selected_population.append(min(temporal_tournament))
            temporal_tournament.clear()

        return selected_population
