from Cut.cut import Cut

class StructureCut(Cut):
    def __init__(self, *args):
        self.amount = int(args[0])
        self.generations = int(args[1])
        self.prev_pop = self.fitness_list(args[2])
        self.prev_pop.sort()
        self.decimals = int(args[3])
        self.curr_generations = 0

    def cut(self, population):
        curr_pop = self.fitness_list(population)
        curr_pop.sort()
        pop_kept = 0
        for i, prev in enumerate(self.prev_pop):
            curr = curr_pop[i]
            diff = round(abs(prev - curr), self.decimals)
            if diff == 0:
                pop_kept += 1   

        if pop_kept >= self.amount:
            self.curr_generations += 1
        else:
            self.curr_generations = 0

        bol = self.curr_generations >= self.generations
        self.prev_pop = curr_pop
        return bol
                
    def fitness_list(self, population):
        l = []
        for char in population:
            l.append(char.get_performance())
        return l