from time import time
from Cut.cut import Cut

class TimeCut(Cut):
    def __init__(self, *args):
        self.time = time()
        self.limit = float(args[0])
    
    def cut(self, population):
        return (time() - self.time) >= self.limit
        