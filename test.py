from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController
from NonInformative.bfs import bfs

player = Player(7, 1)
box = Box(5, 2)
box2 = Box(5, 3)
node = Node(player, [box, box2])
board = Board()
game = GameController(board)


solution = bfs(game, node)
game.print_path(solution.path) if solution.solved else print("sad")
