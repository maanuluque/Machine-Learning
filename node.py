import box
import player
import board


class Node:

    def __init__(self, board, player, boxes):
        self.board = board
        self.player = player
        self.boxes = boxes

    def get_boxes(self):
        return self.boxes

    def get_player(self):
        return self.player

    def get_board(self):
        return self.board

    def is_deadlock(self):
        pass

    def get_children(self):
        pass


