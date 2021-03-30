from abc import ABC, abstractmethod

class Fill(ABC):
    @abstractmethod
    def __init__(self, population_size, children_size):
        self.population_size = population_size
        self.children_size = children_size
        pass

    @abstractmethod
    def fill(self, population, children):
        pass