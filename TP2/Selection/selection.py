from abc import ABC, abstractmethod

class Selection(ABC):
    @abstractmethod
    def __init__(self, population_size, amount):
        self.population_size = population_size
        self.amount = amount
        pass

    @abstractmethod
    def select(self, population):
        pass