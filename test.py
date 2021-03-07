from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController

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

children = game.get_children(node)
for child in children:
    print(f'Player: {child.player.x}, {child.player.y}')
    print(f'~board:  {board.board[child.player.x][child.player.y]}')
    print(f'valid: {board.is_valid_position(child.player.x, child.player.y)}')
    for b in child.boxes:
        print(f'Box: {b.x}, {b.y}')
        print(f'~board: {board.board[b.x][b.y]}')
    print('-----------------------')

