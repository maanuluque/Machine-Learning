class Item:
    # An Item can be a: weapon, boots, gloves, helmet, gloves.
    def __init__(self, type, id, strength, agility, expertise, resistance, health):
        self.type = type
        self.id = id
        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistance = resistance
        self.health = health

    def print_item(self):
        return "type: " + str(self.type) + ", id: " + str(self.id)
