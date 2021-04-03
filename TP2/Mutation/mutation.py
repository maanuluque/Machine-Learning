import random
from abc import ABC, abstractmethod
from items import Items
import util

class Mutation(ABC):
    @abstractmethod
    def __init__(self, children_size, probability, min_h, max_h, height_decimals, items_db):
        self.children_size = children_size
        self.probability = probability
        self.min_h = min_h
        self.max_h = max_h
        self.items_db = items_db
        self.genes_idx = list(range(0, 6))
        self.aux_idx = []
        self.height_decimals = height_decimals

    def mutate(self, children):
        mutated = []
        for child in children:
            mutated.append(self.single_mutation(child))
        return mutated

    @abstractmethod
    def single_mutation(self, child):
        pass

    def mutate_gene(self, child, genes):
        items = [child.items.equipment["weapon"], child.items.equipment["boots"], child.items.equipment["helmet"],
                 child.items.equipment["gloves"], child.items.equipment["chest"]]
        child_height = child.height
        for gene in genes:
            if gene == 1:
                weapon_id = child.items.equipment["weapon"].id
                weapon = None
                while weapon is None or weapon_id == weapon.id:
                    weapon = util.rand_weapon(self.items_db)
                items[0] = weapon

            elif gene == 2:
                boots_id = child.items.equipment["boots"].id
                boots = None
                while boots is None or boots_id == boots.id:
                    boots = util.rand_boots(self.items_db)
                items[1] = boots

            elif gene == 3:
                helmet_id = child.items.equipment["helmet"].id
                helmet = None
                while helmet is None or helmet_id == helmet.id:
                    helmet = util.rand_helmet(self.items_db)
                items[2] = helmet

            elif gene == 4:
                gloves_id = child.items.equipment["gloves"].id
                gloves = None
                while gloves is None or gloves_id == gloves.id:
                    gloves = util.rand_gloves(self.items_db)
                items[3] = gloves

            elif gene == 5:
                chest_id = child.items.equipment["chest"].id
                chest = None
                while chest is None or chest_id == chest.id:
                    chest = util.rand_chest(self.items_db)
                items[4] = chest

            elif gene == 6:
                height = None
                while height is None or height == child.height:
                    height = round(util.rand_height(self.min_h, self.max_h), self.height_decimals)
                child_height = height

        return child.create_child(Items(items[0], items[1], items[2], items[3], items[4]), child_height)
