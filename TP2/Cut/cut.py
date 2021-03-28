from abc import ABC, abstractmethod

class Cut(ABC):
    @abstractmethod
    def __init__(self, limit):
        pass

    @abstractmethod
    def cut(self, *args):
        pass