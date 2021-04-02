from Cut.cut import Cut

class AcceptableCut(Cut):
    def __init__(self, *args):
        self.acceptable_fitness = args[0]
    
    def cut(self, population):
        best_fitness = population[0]
        return best_fitness.performance >= self.acceptable_fitness

