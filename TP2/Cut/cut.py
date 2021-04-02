from abc import ABC, abstractmethod

class Cut(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def cut(self, population):
        pass