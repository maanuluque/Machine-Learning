import random
from Cross.crossover import Crossover
from items import Items

class Uniform(Crossover):

    def __init__(self, parent_size, genome_size, item_keys, probability):
        super().__init__(parent_size, genome_size, item_keys)
        self.probability = probability

    def crossover(self, parent1, parent2):
        items1 = {}
        items2 = {}
        height1 = parent1.height
        height2 = parent2.height
        p1_equipment = parent1.items.equipment
        p2_equipment = parent2.items.equipment

        i = 0
        while i < self.genome_size:
            p = random.random()
            if p >= self.probability:
                if i < self.item_len:
                    items1[self.item_keys[i]] = p2_equipment[self.item_keys[i]]
                    items2[self.item_keys[i]] = p1_equipment[self.item_keys[i]]
                else:
                    height1 = parent2.height
                    height2 = parent1.height
            else:
                if i < self.item_len:
                    items1[self.item_keys[i]] = p1_equipment[self.item_keys[i]]
                    items2[self.item_keys[i]] = p2_equipment[self.item_keys[i]]
            i += 1
            
        child1 = parent1.create_child(
            Items(items1["weapon"], items1["boots"], items1["helmet"], items1["gloves"], items1["chest"]), height1)
        child2 = parent1.create_child(
            Items(items2["weapon"], items2["boots"], items2["helmet"], items2["gloves"], items2["chest"]), height2)
        return child1, child2
