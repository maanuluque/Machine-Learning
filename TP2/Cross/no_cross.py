from Cross.crossover import Crossover

class NoCross(Crossover):
    def __init__(self, genome_size):
        super().__init__(genome_size)

    def cross(self, parents):
        return parents
