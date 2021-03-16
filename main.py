from Heuristics.minimumMatchingLowerBound import mmlb
from Heuristics.simpleLowerBound import slb, slb_plus
from Informative.aStar import a_star
from Informative.idaStar import ida_star
from Informative.globalGreedy import globalGreedy
from goal import Goal
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
    heuristic = data['heuristics']
    heuristic_str = data['heuristics']
    iddfs_depth_limit = data["iddfs_depth_limit"]
    ida_limit = data["ida*_limit"]
    print("Chosen algorithm is:", algorithm)
    print("Board:")
    print()

    with open(game_map) as game_map_file:
        lines = game_map_file.readlines()

    height = len(lines)
    width = len(lines[0]) - 1

    board = [['1' for i in range(width)] for j in range(height)]
    boxes = []
    goals = []
    player = Player(0, 0)

    for x, line in enumerate(lines):
        for y, char in enumerate(line[:-1]):
            if char == constants.PLAYER:
                player = Player(x, y)
                board[x][y] = constants.EMPTY
            elif char == constants.BOX:
                boxes.append(Box(x, y))
                board[x][y] = constants.EMPTY
            elif char == constants.GOAL:
                goals.append(Goal(x, y))
                board[x][y] = char
            else:
                board[x][y] = char

    board = Board(board, height, width, goals)
    board.print_state(player=player, boxes=boxes)

    initial_node = Node(player, boxes)
    game = GameController(board)
    if heuristic == "slb":
        heuristic = slb
    elif heuristic == "mmlb":
        heuristic = mmlb
    elif heuristic == "slb*":
        heuristic = slb_plus

    if algorithm == "bfs":
        game_solution = bfs(game, initial_node)
    elif algorithm == "dfs":
        game_solution = dfs(game, initial_node)
    elif algorithm == "iddfs":
        game_solution = iddfs(game, initial_node, iddfs_depth_limit)
    elif algorithm == "A*":
        game_solution = a_star(game, initial_node, board, heuristic)
    elif algorithm == "globalGreedy":

        game_solution = globalGreedy(game, initial_node, board, heuristic)
    elif algorithm == "IDA*":
        game_solution = ida_star(game, initial_node, board, heuristic, ida_limit)

    else:
        print("Invalid algorithm. See you later")
        exit()

    if game_solution.solved:
        print('Solution found:')
        game.print_path(game_solution.path)
        print("Solution depth: ", game_solution.depth)
    else:
        print("Solution not found.")

    print("Expanded nodes: ", game_solution.expanded)
    print("Frontier nodes: ", game_solution.leaves)
    print("Processing time: ", round(game_solution.processing_time, 4))
    print("Memory used: " + str(game_solution.space_complexity) + " bytes")
    print()
    print("Chosen algorithm is:", algorithm)
    if algorithm == "A*" or algorithm == "IDA*" or algorithm == "globalGreedy*":
        print("Chosen heuristic is:", heuristic_str)


if __name__ == "__main__":
    main()
