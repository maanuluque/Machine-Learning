from abc import abstractmethod, ABC

class Crossover(ABC):
    @abstractmethod
    def __init__(self, parents_size, genome_size):
        self.parents_size = parents_size
        self.genome_size = genome_size
        pass

    @abstractmethod
    def cross(self, parents):
        pass
