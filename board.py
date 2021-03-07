import agent


class Board:

    def __init__(self):
        self.size = 8  # Puse cualquier cosa para que me saque un error
        self.width = 14
        self.board = [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "0", "0", "0", "0", "+", "+", "0", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ]

    def whereIsP(self, board):
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 'P':
                    return x, y
        return 0, 0

    def is_valid_position(self, x, y):
        return x in range(0, self.size) and y in range(0, self.width) and self.board[x][y] != "1"

