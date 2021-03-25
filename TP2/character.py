from abc import ABC, abstractmethod
import math
import items


class Character(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_performance(self, attack, defense):
        pass

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

class Warrior(Character):
    def __init__(self, items, height):
        print("I am a Warrior")
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = super().set_modifiers(height)

        self.attack = self.set_attack(items, self.attack_modifier)
        self.defense = self.set_defense(items, self.defense_modifier)
        self.performance = self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.6 * attack + 0.6 * defense


class Archer(Character):
    def __init__(self, items, height):
        print("I am an Archer")
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = super().set_modifiers(height)
        self.attack = (self.items.stats["p_agility"] + self.items.stats["p_expertise"]) * self.items.stats[
            "p_strength"] * self.attack_modifier
        self.defense = (self.items.stats["p_resistance"] + self.items.stats["p_expertise"]) * self.items.stats[
            "p_health"] * self.defense_modifier
        self.performance = self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.9 * attack + 0.1 * defense


class Defender(Character):
    def __init__(self, items, height):
        print("I am a Defender")
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = super().set_modifiers(height)
        self.attack = (self.items.stats["p_agility"] + self.items.stats["p_expertise"]) * self.items.stats[
            "p_strength"] * self.attack_modifier
        self.defense = (self.items.stats["p_resistance"] + self.items.stats["p_expertise"]) * self.items.stats[
            "p_health"] * self.defense_modifier
        self.performance = self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.3 * attack + 0.8 * defense


class Infiltrate(Character):
    def __init__(self, items, height):
        print("I am an Infiltrate")
        self.items = items
        self.height = height
        self.attack_modifier, self.defense_modifier = super().set_modifiers(height)
        self.attack = (self.items.stats["p_agility"] + self.items.stats["p_expertise"]) * self.items.stats[
            "p_strength"] * self.attack_modifier
        self.defense = (self.items.stats["p_resistance"] + self.items.stats["p_expertise"]) * self.items.stats[
            "p_health"] * self.defense_modifier
        self.performance = self.set_performance(self.attack, self.defense)

    def set_performance(self, attack, defense):
        return 0.8 * attack + 0.3 * defense
