from abc import abstractmethod, ABC


class Crossover(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cross(self, parents):
        pass
