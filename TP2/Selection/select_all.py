from Selection.selection import Selection

class SelectAll(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        return population[:self.amount]