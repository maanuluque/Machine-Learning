class Node:

    def __init__(self, player, boxes: list):
        self.player = player
        self.boxes = boxes

    def __hash__(self):
        return hash((self.player, tuple(self.boxes)))

    def __eq__(self, other):
        if not self.player == other.player or not len(self.boxes) == len(other.boxes):
            return False
        for box in self.boxes:
            if box not in other.boxes:
                return False
        return True
