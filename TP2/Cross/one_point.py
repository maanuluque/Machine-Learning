import random
from Cross.crossover import Crossover
from items import Items


class OnePointCross(Crossover):

    def __init__(self, parents_size, genome_size):
        super().__init__(parents_size, genome_size)

    def crossover(self, parent1, parent2):
        p = random.randint(0, self.genome_size)
        parent_keys = list(parent1.items.equipment.keys())

        item_len = len(parent_keys)

        items1 = {}
        items2 = {}
        height1 = parent1.height
        height2 = parent2.height

        for i in range(self.genome_size):
            if i >= p:
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