from time import time
from Cut.cut import Cut

class GenerationsCut(Cut):
    def __init__(self, limit):
        self.limit = int(limit)
    
    def cut(self, *args):
        self.limit -= 1
        return self.limit <= 0
        