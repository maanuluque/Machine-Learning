from abc import ABC, abstractmethod
from items import Items
from main import rand_helmet, rand_weapon, rand_boots, rand_gloves, rand_chest, rand_height


class Mutation(ABC):
    @abstractmethod
    def __init__(self, children_size, probability, min_h, max_h, items_db):
        self.children_size = children_size
        self.probability = probability
        self.min_h = min_h
        self.max_h = max_h
        self.items_db = items_db

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
                    weapon = rand_weapon(self.items_db)
                    weapon_id = weapon.id
                items[0] = weapon

            elif gene == 2:
                boots_id = child.items.equipment["boots"].id
                boots = None
                while boots is None or boots_id == boots.id:
                    boots = rand_boots(self.items_db)
                    boots_id = boots.id
                items[1] = boots

            elif gene == 3:
                helmet_id = child.items.equipment["helmet"].id
                helmet = None
                while helmet is None or helmet_id == helmet.id:
                    helmet = rand_helmet(self.items_db)
                    helmet_id = helmet.id
                items[2] = helmet

            elif gene == 4:
                gloves_id = child.items.equipment["gloves"].id
                gloves = None
                while gloves is None or gloves_id == gloves.id:
                    gloves = rand_gloves(self.items_db)
                    gloves_id = gloves.id
                items[3] = gloves

            elif gene == 5:
                chest_id = child.items.equipment["chest"].id
                chest = None
                while chest is None or chest_id == chest.id:
                    chest = rand_chest(self.items_db)
                    chest_id = chest.id
                items[4] = chest

            elif gene == 6:
                height = None
                while height is None or height == child.height:
                    height = rand_height(self.min_h, self.max_h)
                child_height = height
        return child.create_child(Items(items[0], items[1], items[2], items[3], items[4]), child_height)
