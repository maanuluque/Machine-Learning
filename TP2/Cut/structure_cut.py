from Cut.cut import Cut

class StructureCut(Cut):
    def __init__(self, *args):
        self.amount = int(args[0])
        self.generations = int(args[1])
        self.prev_pop = self.fitness_list(args[2])
        self.decimals = int(args[3])
        self.curr_generations = 0

    def cut(self, population):
        curr_pop = self.fitness_list(population)
        pop_kept = 0
        for i, prev in enumerate(self.prev_pop):
            if round(abs(prev - curr_pop[i])) == 0:
                pop_kept += 1   

        if pop_kept >= self.amount:
            self.curr_generations += 1
            print('+1 generations')
        else:
            self.curr_generations = 0
            print('reset generations')

        bol = self.curr_generations >= self.generations
        print(f'Cut: {bol}')
        return bol
                

    def fitness_list(self, population):
        l = []
        for char in population:
            l.append(char.performance)
        return l