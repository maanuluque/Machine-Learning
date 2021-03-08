from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController
from NonInformative.bfs import bfs
from solution import Solution
import json

with open('config.json') as config_file:
    data = json.load(config_file)
    config_file.close()

algorithm = data['algorithm']
game_map = data['map']
print(algorithm)
print(game_map)

with open(game_map) as game_map_file:
    lines = game_map_file.readlines()
    game_map_file.close()


height = len(lines)
width = len(lines[0])-1

board = [['0' for i in range(width)] for j in range(height)]
boxes = []
player = Player(0, 0)

for x, line in enumerate(lines):
    for y, char in enumerate(line[:-1]):
        if char == 'P':
            player = Player(x, y)
            board[x][y] = '.'
        elif char == '#':
            boxes.append(Box(x, y))
            board[x][y] = '.'
        else:
            board[x][y] = char

print(height)
print(width)
board = Board(board, height, width)
board.print_state(player=player, boxes=boxes)

node = Node(player, boxes)
game = GameController(board)


game_solution = bfs(game, node)
game.print_path(game_solution.path) if game_solution.solved else print("sad")
print(game_solution.processing_time) if game_solution.solved else print("sad")

def solve(algorithm, controller, root, heuristics):
    solution = Solution(None, None, None, None, False, None, None)
    if "bfs" in algorithm:
        solution = bfs(controller, root)
    elif "dfs" in algorithm:
        solution = None  # dfs()
    #
    #
    return solution
