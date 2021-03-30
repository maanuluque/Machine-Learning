from SIA.TP2.Selection.selection import Selection
from SIA.TP2.sortedListAdapter import SortedListAdapter



class Elite(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        selected_population = []
        sorted_population = SortedListAdapter()
        population_size = len(population)

        for x in range(population_size):
            sorted_population.append(population[x])

        for x in range(self.amount):
            selected_population.append(sorted_population.pop())

        return selected_population

