import copy as cp
from node import Node

class GameController:
    def __init__(self, board):
        self.board = board
        self.moves = [(-1, 0), (0, -1), (0, 1), (1, 0)] # up,  left, right, down
    
    def get_children(self, node):
        # Is it worth it?
        # if not self.board.valid_node(node):
        #     return None
        
        x = node.player.x
        y = node.player.y
        children = []
        for move in self.moves:
            child = self.make_move(node, move) if self.can_move(node, move) else None
            if child:
                children.append(child)
        return children

    def make_move(self, node, move):
        child = Node(cp.deepcopy(node.player), cp.deepcopy(node.boxes))
        child.player.x += move[0]
        child.player.y += move[1]
        for box in child.boxes:
            if box.x == child.player.x and box.y == child.player.y:
                box.x += move[0]
                box.y += move[1]
                break
        return child

    def can_move(self, node, move):
        next_x = node.player.x + move[0]
        next_y = node.player.y + move[1]
        if not self.board.is_valid_position(next_x, next_y):
            return False
        n_next_x = next_x + move[0]
        n_next_y = next_y + move[1]
        moving_box = False
        blocking_box = False
        for box in node.boxes:
            if box.x == next_x and box.y == next_y:
                if blocking_box or not self.board.is_valid_position(n_next_x, n_next_y):
                    return False
                moving_box = True
            if box.x == n_next_x and box.y == n_next_y:
                if moving_box:
                    return False
                blocking_box = True
        return True

    def is_solution(self, node):
        # TODO
        return False

    def is_deadlock(self, node):
        # TODO
        return False

