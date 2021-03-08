from player import Player
from box import Box
from node import Node
from board import Board
from gameController import GameController
from NonInformative.bfs import bfs
from NonInformative.dfs import dfs
from solution import Solution
import json

def solve(algorithm, controller, root, heuristics):
    solution = Solution(None, None, None, None, False, None, None)
    if "bfs" in algorithm:
        solution = bfs(controller, root)
    elif "dfs" in algorithm:
        solution = None  # dfs()
    #
    #
    return solution

def main():
    # Game Setup
    with open('config.json') as config_file:
        data = json.load(config_file)

    algorithm = data['algorithm']
    game_map = data['map']
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
            if char == 'P':
                player = Player(x, y)
                board[x][y] = '.'
            elif char == '#':
                boxes.append(Box(x, y))
                board[x][y] = '.'
            else:
                board[x][y] = char

    # Debugging
    # -------------------------
    # print(height)
    # print(width)
    # ------------------------

    board = Board(board, height, width)
    board.print_state(player=player, boxes=boxes)

    initial_node = Node(player, boxes)
    game = GameController(board)

    if algorithm == "bfs":
        game_solution = bfs(game, initial_node)
        if game_solution.solved:
            game.print_path(game_solution.path)
            print("Processing time: ", game_solution.processing_time)
        else:
            print("Solution not found.")
    elif algorithm == "dfs":
        game_solution = dfs(game, initial_node)
        if game_solution.solved:
            game.print_path(game_solution.path)
            print("Processing time: ", game_solution.processing_time)
        else:
            print("Solution not found.")


if __name__ == "__main__":
    main()