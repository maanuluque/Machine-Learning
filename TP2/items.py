import math


class Items:
    # Each parameter is an ITEM instance.
    def __init__(self, weapon, boots, helmet, gloves, chest):
        self.equipment = {
            "weapon": weapon,
            "boots": boots,
            "helmet": helmet,
            "gloves": gloves,
            "chest": chest
        }

        self.stats = self.calculate_stats()

    def calculate_stats(self):
        total_strength = 0
        total_agility = 0
        total_expertise = 0
        total_resistance = 0
        total_health = 0
        for key in self.equipment.keys():
            total_strength += self.equipment[key].strength
            total_agility += self.equipment[key].agility
            total_expertise += self.equipment[key].expertise
            total_resistance += self.equipment[key].resistance
            total_health += self.equipment[key].health

        items_stats = {
            "p_strength": 100 * math.tanh(0.01 * total_strength),
            "p_agility": math.tanh(0.01 * total_agility),
            "p_expertise": 0.6 * math.tanh(0.01 * total_expertise),
            "p_resistance": math.tanh(0.01 * total_resistance),
            "p_health": 100 * math.tanh(0.01 * total_health)
        }

        return items_stats
