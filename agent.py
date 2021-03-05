class Agent:

    def __init__(self):
        self.row = 0
        self.col = 0

    def setPosition(self, row, col):
        self.row = row
        self.col = col

    def getPosition(self):
        return self.row, self.col