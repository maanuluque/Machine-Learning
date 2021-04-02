from abc import abstractmethod, ABC
import random


class Crossover(ABC):
    @abstractmethod
    def __init__(self, parent_size, genome_size, item_keys):
        self.genome_size = genome_size
        self.parent_size = parent_size
        self.item_keys = item_keys
        self.item_len = len(item_keys)
        self.index_list = list(range(0, parent_size))
        self.aux = []
        pass

    def cross(self, parents):
        children = []
        parent2 = None
        size = self.parent_size
        while size >= 2:
            x = random.randint(0, size - 1)
            size = size - 1
            idx = self.index_list.pop(x)
            self.aux.append(idx)
            parent1 = parents[idx]

            x = random.randint(0, size -1)
            size = size - 1
            idx = self.index_list.pop(x)
            self.aux.append(idx)
            parent2 = parents[idx]

            children.extend(self.crossover(parent1, parent2))
        if size == 1:
            idx = self.index_list.pop()
            self.aux.append(idx)
            parent1 = parents[idx]
            if parent2:
                children.append(self.crossover(parent1, parent2)[0])  # return 1 child to maintain numbers through gen
            else:
                children.append(parent1)

        self.index_list = self.aux
        self.aux = []
        return children

    @abstractmethod
    def crossover(self, parent1, parent2):
        pass
