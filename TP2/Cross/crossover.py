from abc import abstractmethod, ABC
import random


class Crossover(ABC):
    @abstractmethod
    def __init__(self, parent_size, genome_size):
        self.genome_size = genome_size
        self.parent_size = parent_size
        pass

    def cross(self, parents):
        children = []
        parent_list = parents.copy()
        parent2 = None
        size = self.parent_size
        while size >= 2:
            x = random.randint(0, size - 1)
            size = size - 1
            parent1 = parent_list.pop(x)
            x = random.randint(0, size -1)
            size = size - 1
            parent2 = parent_list.pop(x)
            children.extend(self.crossover(parent1, parent2))
        if len(parent_list) == 1:
            parent1 = parent_list.pop()
            if parent2:
                children.append(self.crossover(parent1, parent2)[0])  # return 1 child to maintain numbers through gen
            else:
                children.append(parent1)
        return children

    @abstractmethod
    def crossover(self, parent1, parent2):
        pass
