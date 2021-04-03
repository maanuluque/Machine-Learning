from Cut.cut import Cut

class AcceptableCut(Cut):
    def __init__(self, *args):
        self.acceptable_fitness = args[0]
    
    def cut(self, population):
        best_fitness = min(population)
        return best_fitness.get_performance() >= self.acceptable_fitness
