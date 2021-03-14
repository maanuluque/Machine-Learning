import constants


class Board:

    def __init__(self, board, height, width, goals):
        self.board = board
        self.size = height
        self.width = width
        self.goals = goals

    def is_valid_position(self, x, y):
        return x in range(0, self.size) and y in range(0, self.width) and self.board[x][y] != constants.WALL

    def is_solution(self, boxes):
        for box in boxes:
            if self.board[box.x][box.y] != constants.GOAL:
                return False
        return True

    def is_deadlock(self, boxes):
        for box in boxes:
            if self.board[box.x-1][box.y] == constants.GOAL:
                return False
            if self.board[box.x-1][box.y] == constants.WALL and self.board[box.x][box.y-1] == constants.WALL:
                return True
            if self.board[box.x+1][box.y] == constants.WALL and self.board[box.x][box.y-1] == constants.WALL:
                return True
            if self.board[box.x-1][box.y] == constants.WALL and self.board[box.x][box.y+1] == constants.WALL:
                return True
            if self.board[box.x+1][box.y] == constants.WALL and self.board[box.x][box.y+1] == constants.WALL:
                return True
        return False

    def print_state(self, player, boxes):
        for x, line in enumerate(self.board):
            for y, column in enumerate(line):
                if player.x == x and player.y == y:
                    print(constants.PLAYER, end=' ')
                else:
                    for box in boxes:
                        if box.x == x and box.y == y:
                            if column == '+':
                                print(constants.BOX_IN_GOAL, end=' ')
                            else:
                                print(constants.BOX, end=' ')
                            break
                    else:
                        print(column, end=' ')
            print()
        print()
