from Cross.crossover import Crossover

class NoCross(Crossover):
    def __init__(self, parents_size, genome_size):
        super().__init__(parents_size, genome_size)

    def cross(self, parents):
        return parents
