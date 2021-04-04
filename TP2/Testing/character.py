from abc import ABC, abstractmethod
import math


class Character(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_performance(self, attack, defense):
        pass

    def get_performance(self):
        if self.performance == None:
            self.performance = self.set_performance(self.get_attack(), self.get_defense())
        return self.performance

    def get_attack(self):
        if self.attack == None:
            self.attack_modifier, self.defense_modifier = self.set_modifiers(self.height)
            self.attack  = self.set_attack(self.items, self.attack_modifier)
            self.defense = self.set_defense(self.items, self.defense_modifier)
        return self.attack

    def get_defense(self):
        if self.defense == None:
            self.attack_modifier, self.defense_modifier = self.set_modifiers(self.height)
            self.attack  = self.set_attack(self.items, self.attack_modifier)
            self.defense = self.set_defense(self.items, self.defense_modifier)
        return self.defense    

    def set_modifiers(self, height):
        atm = 0.7 - math.pow((3 * height - 5), 4) + math.pow((3 * height - 5), 2) + (height / 4)
        dfm = 1.9 + math.pow((2.5 * height - 4.16), 4) - math.pow((2.5 * height - 4.16), 2) - (3 * height / 10)
        return atm, dfm

    def set_attack(self, items, attack_modifier):
        attack = (items.stats["p_agility"] + items.stats["p_expertise"]) * items.stats[
            "p_strength"] * attack_modifier
        return attack

    def set_defense(self, items, defense_modifier):
        defense = (items.stats["p_resistance"] + items.stats["p_expertise"]) * items.stats[
            "p_health"] * defense_modifier
        return defense

    def print_character(self):
        print(f"====> Fitness: {self.get_performance()}")
        print(f"Height: {self.height}")
        self.print_items()
        print(f"Type: {self.type} <====")

    def print_items(self):
        for k, v in self.items.equipment.items():
            print("Item: { " + v.print_item() + " }")

    def __lt__(self, other):
        return other.get_performance().__lt__(self.get_performance())


class Warrior(Character):
    def __init__(self, items, height):
        self.type = "Warrior"
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = None, None # super().set_modifiers(height)

        self.attack = None # self.set_attack(items, self.attack_modifier)
        self.defense = None # self.set_defense(items, self.defense_modifier)
        self.performance = None # self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.6 * attack + 0.6 * defense

    def create_child(self, items, height):
        return Warrior(items, height)

class Archer(Character):
    def __init__(self, items, height):
        self.type = "Archer"
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = None, None # super().set_modifiers(height)

        self.attack = None # self.set_attack(items, self.attack_modifier)
        self.defense = None # self.set_defense(items, self.defense_modifier)
        self.performance = None # self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.9 * attack + 0.1 * defense

    def create_child(self, items, height):
        return Archer(items, height)


class Defender(Character):
    def __init__(self, items, height):
        self.type = "Defender"
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = None, None # super().set_modifiers(height)

        self.attack = None # self.set_attack(items, self.attack_modifier)
        self.defense = None # self.set_defense(items, self.defense_modifier)
        self.performance = None # self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.3 * attack + 0.8 * defense

    def create_child(self, items, height):
        return Defender(items, height)


class Infiltrate(Character):
    def __init__(self, items, height):
        self.type = "Infiltrate"
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = None, None # super().set_modifiers(height)

        self.attack = None # self.set_attack(items, self.attack_modifier)
        self.defense = None # self.set_defense(items, self.defense_modifier)
        self.performance = None # self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.8 * attack + 0.3 * defense

    def create_child(self, items, height):
        return Infiltrate(items, height)