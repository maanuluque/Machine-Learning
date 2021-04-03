from Cut.cut import Cut

class ContentCut(Cut):
    def __init__(self, *args):
        self.generations = int(args[0])
        self.decimals = int(args[1])
        self.prev_best = 0
        self.curr_generations = 0

    def cut(self, population):
        curr_best = round(min(population).get_performance(), self.decimals)

        if curr_best == self.prev_best:
            self.curr_generations += 1
        else:
            self.curr_generations = 0
            self.prev_best = curr_best

        return self.curr_generations >= self.generations