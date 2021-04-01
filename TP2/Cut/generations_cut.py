from Cut.cut import Cut

class GenerationsCut(Cut):
    def __init__(self, *args):
        self.limit = int(args[0])
    
    def cut(self, population):
        self.limit -= 1
        return self.limit < 0
        