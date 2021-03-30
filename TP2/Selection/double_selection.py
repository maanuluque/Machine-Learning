from abc import ABC, abstractmethod
from Selection.selection import Selection

class DoubleSelection(Selection):
    def __init__(self, select_1, select_2):
        self.select_1 = select_1
        self.select_2 = select_2

    def select(self, population):
        children_1 = self.select_1.select(population)
        children_2 = self.select_2.select(population)
        children_1.extend(children_2)
        return children_1