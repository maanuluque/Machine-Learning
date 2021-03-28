from abc import ABC, abstractmethod

class Mutation(ABC):
    @abstractmethod
    def __init__(self, children_size, probability):
        self.children_size = children_size
        self.probability = probability
        pass

    @abstractmethod
    def mutate(self, children):
        pass