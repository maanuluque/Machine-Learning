from Selection.selection import Selection

class Elite(Selection):
    def __init__(self, population_size, amount):
        super().__init__(population_size, amount)

    def select(self, population):
        if self.amount == self.population_size:
            return population

        to_select = self.amount
        selected = []
        
        while to_select >= self.population_size:
            if (to_select == self.population_size):
                return population
            selected.extend(population)
            to_select -= self.population_size
        
        if to_select > 0:
            sorted_pop = population.copy()
            sorted_pop.sort()
            selected.extend(sorted_pop[:to_select])

        return selected
        