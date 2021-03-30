from Cut.cut import Cut

class AcceptableCut(Cut):
    def __init__(self, acceptable_fitness):
        self.acceptable_fitness = acceptable_fitness
    
    def cut(self, *args):
        population = args[0]
        best_fitness = population[0] # TODO will population be List or PQ??
        return best_fitness.performance >= self.acceptable_fitness

