from time import time

class TimeCut:
    def __init__(self, limit):
        print(f'Limit: {limit}')
        self.time = time()
        self.limit = float(limit)
    
    def cut(self):
        return (time() - self.time) >= self.limit
        