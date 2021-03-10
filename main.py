from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController
from NonInformative.bfs import bfs
from NonInformative.dfs import dfs
from NonInformative.iddfs import iddfs
import constants

from solution import Solution
import json


#  TODO delete??
# def solve(algorithm, controller, root, heuristics):
#     solution = Solution(None, None, None, None, False, None, None)
#     if "bfs" in algorithm:
#         solution = bfs(controller, root)
#     elif "dfs" in algorithm:
#         solution = None  # dfs()
#     #
#     #
#     return solution

def main():
    # Game Setup
    with open('config.json') as config_file:
        data = json.load(config_file)

    algorithm = data['algorithm']
    game_map = data['map']
    iddfs_depth_limit = data["iddfs_depth_limit"]
    print("Chosen algorithm is:", algorithm)
    print("Board:")
    print()

    with open(game_map) as game_map_file:
        lines = game_map_file.readlines()

    height = len(lines)
    width = len(lines[0]) - 1

    board = [['0' for i in range(width)] for j in range(height)]
    boxes = []
    player = Player(0, 0)

    for x, line in enumerate(lines):
        for y, char in enumerate(line[:-1]):
            if char == constants.PLAYER:
                player = Player(x, y)
                board[x][y] = constants.EMPTY
            elif char == constants.BOX:
                boxes.append(Box(x, y))
                board[x][y] = constants.EMPTY
            else:
                board[x][y] = char

    board = Board(board, height, width)
    board.print_state(player=player, boxes=boxes)

    initial_node = Node(player, boxes)
    game = GameController(board)

    if algorithm == "bfs":
        game_solution = bfs(game, initial_node)
    elif algorithm == "dfs":
        game_solution = dfs(game, initial_node)
    elif algorithm == "iddfs":
        game_solution = iddfs(game, initial_node, iddfs_depth_limit)
    else:
        print("Invalid algorithm. See you later")
        exit()

    if game_solution.solved:
        print('Solution found:')
        game.print_path(game_solution.path)
        print("Solution depth: ", game_solution.depth)
        print("Solution cost: ", game_solution.cost)
    else:
        print("Solution not found.")

    print("Processing time: ", game_solution.processing_time)
    print("Expanded nodes: ", game_solution.expanded)
    print("Frontier nodes: ", game_solution.leaves)

if __name__ == "__main__":
    main()