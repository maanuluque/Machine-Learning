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

    def switch_genes(self, child, gen):
        if gen == 1:
            weapon_id = child.items.equipment["weapon"].id
            weapon = None
            while weapon is None or weapon_id == weapon.id:
                weapon = rand_weapon(self.items_db)
                weapon_id = weapon.id
            child = child.create_child(Items(weapon, child.items.equipment["boots"], child.items.equipment["helmet"],
                                             child.items.equipment["gloves"], child.items.equipment["chest"]),
                                       child.height)

        elif gen == 2:
            boots_id = child.items.equipment["boots"].id
            boots = None
            while boots is None or boots_id == boots.id:
                boots = rand_boots(self.items_db)
                boots_id = boots.id
            child = child.create_child(Items(child.items.equipment["weapon"], boots, child.items.equipment["helmet"],
                                             child.items.equipment["gloves"], child.items.equipment["chest"]),
                                       child.height)

        elif gen == 3:
            helmet_id = child.items.equipment["helmet"].id
            helmet = None
            while helmet is None or helmet_id == helmet.id:
                helmet = rand_helmet(self.items_db)
                helmet_id = helmet.id
            child = child.create_child(Items(child.items.equipment["weapon"], child.items.equipment["boots"], helmet,
                                             child.items.equipment["gloves"], child.items.equipment["chest"]),
                                       child.height)
        elif gen == 4:
            gloves_id = child.items.equipment["gloves"].id
            gloves = None
            while gloves is None or gloves_id == gloves.id:
                gloves = rand_gloves(self.items_db)
                gloves_id = gloves.id
            child = child.create_child(
                Items(child.items.equipment["weapon"], child.items.equipment["boots"], child.items.equipment["helmet"],
                      gloves, child.items.equipment["chest"]), child.height)
        elif gen == 5:
            chest_id = child.items.equipment["chest"].id
            chest = None
            while chest is None or chest_id == chest.id:
                chest = rand_chest(self.items_db)
                chest_id = chest.id
            child = child.create_child(
                Items(child.items.equipment["weapon"], child.items.equipment["boots"], child.items.equipment["helmet"],
                      child.items.equipment["gloves"], chest), child.height)
        elif gen == 6:
            height = None
            while height is None or height == child.height:
                height = rand_height(self.min_h, self.max_h)
            child = child.create_child(
                Items(child.items.equipment["weapon"], child.items.equipment["boots"], child.items.equipment["helmet"],
                      child.items.equipment["gloves"], child.items.equipment["chest"]), height)
        return child
