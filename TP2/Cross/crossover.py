from abc import abstractmethod, ABC
import random


class Crossover(ABC):
    @abstractmethod
    def __init__(self, genome_size):
        self.genome_size = genome_size
        pass

    def cross(self, parents):
        children = []
        parent2 = None
        while len(parents) >= 2:
            x = random.randint(0, len(parents) - 1)
            parent1 = parents.pop(x)
            x = random.randint(0, len(parents) - 1)
            parent2 = parents.pop(x)
            children.extend(self.crossover(parent1, parent2))
        if len(parents) == 1:
            parent1 = parents.pop()
            if parent2:
                children.append(self.crossover(parent1, parent2)[0])  # return 1 child to maintain numbers through gen
            else:
                children.append(parent1)
        return children

    @abstractmethod
    def crossover(self, parent1, parent2):
        pass
