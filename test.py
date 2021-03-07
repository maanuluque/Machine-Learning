from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController
from NonInformative.bfs import bfs

player = Player(6, 2)
box = Box(6, 1)
box2 = Box(5, 2)
node = Node(player, [box, box2])
board = Board()
game = GameController(board)

print('Board:')
for line in board.board:
    for cell in line:
        print(cell, end=' ')
    print()

print(f'Player: {player.x},{player.y}')
print(f'Box: {box.x},{box.y}')
print(f'Box2: {box2.x},{box2.y}')

print('Moves:')

solution = bfs(game, node)
print(solution.solved)
