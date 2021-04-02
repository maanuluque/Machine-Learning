from Selection.selection import Selection

class Elite(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        population_size = len(population)
        selected_population = []
        sorted_population = []

        for x in range(population_size):
            sorted_population.append(population[x])
        sorted_population.sort()

        for x in range(self.amount):
            selected_population.append(sorted_population.pop(0))

        return selected_population
