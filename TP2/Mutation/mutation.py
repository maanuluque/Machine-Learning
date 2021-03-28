from abc import ABC, abstractmethod

class Mutation(ABC):
    @abstractmethod
    def __init__(self, probability):
        self.probability = probability
        pass

    @abstractmethod
    def mutate(self, children):
        pass