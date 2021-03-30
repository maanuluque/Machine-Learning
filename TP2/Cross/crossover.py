from abc import abstractmethod, ABC
import random

class Crossover(ABC):
    @abstractmethod
    def __init__(self, parents_size, genome_size):
        self.parents_size = parents_size
        self.genome_size = genome_size
        pass

    def cross(self, parents):
        children = []
        while len(parents) >= 2:
            x = random.randint(0, len(parents) - 1)
            parent1 = parents.pop(0)
            x = random.randint(0, len(parents) - 1)
            parent2 = parents.pop(0)
            children.extend(self.crossover(parent1, parent2))
        return children

    @abstractmethod
    def crossover(self, parent1, parent2):
        pass
