from board import Board
from agent import Agent
from gameController import GameController
import NonInformative.dfs as bfs

def main():
    # Set Game Board
    visited = {}
    board = Board()
    gameBoard = board.generateBoard()
    for x in range(len(gameBoard)):
        for y in range(len(gameBoard[x])):
            print(gameBoard[x][y], end='')
            visited[(x, y)] = False
        print()

    print(visited)
    # Set agent's initial position
    agent = Agent()
    x, y = board.whereIsP(gameBoard)
    agent.setPosition(x, y)


    # Set the game controller (in charge of moves, board record, etc)
    gameController = GameController(gameBoard, agent)

    # In this case, BFS



    # Chance to change algorithm

    print("Agent initial position is: ", agent.row, agent.col)

if __name__ == "__main__":
    main()