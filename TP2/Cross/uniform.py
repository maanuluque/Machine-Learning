import random

from Cross.crossover import Crossover
from items import Items


class Uniform(Crossover):

    def __init__(self, genome_size, probability):
        super().__init__(genome_size)
        self.genome_size = genome_size
        self.probability = probability

    def crossover(self, parent1, parent2):
        parent_keys = list(parent1.items.equipment.keys())

        item_len = len(parent_keys)

        items1 = {}
        items2 = {}
        height1 = parent1.height
        height2 = parent2.height

        for i in range(self.genome_size):
            p = random.random()
            if p >= self.probability:
                if i < item_len:
                    items1[parent_keys[i]] = parent2.items.equipment[parent_keys[i]]
                    items2[parent_keys[i]] = parent1.items.equipment[parent_keys[i]]
                else:
                    height1 = parent2.height
                    height2 = parent1.height
            else:
                if i < item_len:
                    items1[parent_keys[i]] = parent1.items.equipment[parent_keys[i]]
                    items2[parent_keys[i]] = parent2.items.equipment[parent_keys[i]]

        child1 = parent1.create_child(
            Items(items1["weapon"], items1["boots"], items1["helmet"], items1["gloves"], items1["chest"]), height1)
        child2 = parent1.create_child(
            Items(items2["weapon"], items2["boots"], items2["helmet"], items2["gloves"], items2["chest"]), height2)
        return child1, child2
