from time import time
from Cut.cut import Cut

class TimeCut(Cut):
    def __init__(self, limit):
        self.time = time()
        self.limit = float(limit)
    
    def cut(self, *args):
        return (time() - self.time) >= self.limit
        