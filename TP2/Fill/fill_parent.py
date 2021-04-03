from Fill.fill import Fill

class FillParent(Fill):
    def __init__(self, population_size, children_size):
        super().__init__(population_size, children_size)

    def fill(self, population, children):
        if self.children_size > self.population_size:
            population.clear()
            population.extend(children)
            new_generation = []
        else:
            new_generation = children
        return new_generation