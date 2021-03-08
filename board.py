class Board:

    def __init__(self):
        self.size = 8  # Puse cualquier cosa para que me saque un error
        self.width = 14
        self.board = [
            ["1", "1", "1", "1", "1", "1"],
            ["1", ".", "+", "+", ".", "1"],
            ["1", ".", ".", ".", ".", "1"],
            ["1", ".", ".", ".", ".", "1"],
            ["1", ".", "1", ".", ".", "1"],
            ["1", ".", ".", ".", ".", "1"],
            ["1", ".", ".", ".", ".", "1"],
            ["1", ".", ".", ".", ".", "1"],
            ["1", "1", "1", "1", "1", "1"],

        ]

    def __init__(self, board, height, width):
        self.board = board
        self.size = height
        self.width = width

    def whereIsP(self, board):
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 'P':
                    return x, y
        return 0, 0

    def is_valid_position(self, x, y):
        return x in range(0, self.size) and y in range(0, self.width) and self.board[x][y] != "1"

    def is_solution(self, boxes):
        for box in boxes:
            if self.board[box.x][box.y] != '+':
                return False
        return True

    def print_state(self, player, boxes):
        for x, line in enumerate(self.board):
            for y, column in enumerate(line):
                if player.x == x and player.y == y:
                    print('P', end=' ')
                else:
                    for box in boxes:
                        if box.x == x and box.y == y:
                            if column == '+':
                                print('X', end=' ')
                            else:
                                print('#', end=' ')
                            break
                    else:
                        print(column, end=' ')
            print()
        print()