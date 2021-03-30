from Fill.fill import Fill

class FillAll(Fill):
    def __init__(self, population_size, children_size):
        super().__init__(population_size, children_size)

    def fill(self, population, children):
        population.extend(children)
        new_generation = []
        return population, new_generation