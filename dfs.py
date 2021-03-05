from gameController import GameController as gc

# Needs a board (not the class, only the list) and the current player position

def dfs(board, row, col):
    visited = {}
    boardRows = len(board)
    boardCols = len(board[0])

    for x in range(boardRows):
        for y in range(boardCols):
            visited[(x,y)] = False          # TODO: CHECK

    visited[(row, col)] = True

    # Left Move
    if not outOfBoundry(boardRows, boardCols, row, col-1):
        leftBoard = gc.makeMove(board, row, col, row, col-1)
        #visited[(row, col-1)] = True
        dfsRec(leftBoard, row, col-1)

    # Up Move
    if not outOfBoundry(boardRows, boardCols, row-1, col):
        upBoard = gc.makeMove(board, row, col, row-1, col)
        #visited[(row-1, col)] = True

        dfsRec(upBoard, row-1, col)

    # Right Move
    if not outOfBoundry(boardRows, boardCols, row, col+1):
        rightBoard = gc.makeMove(board, row, col, row, col+1)
        #visited[(row, col+1)] = True

        dfsRec(rightBoard, row, col+1)

    # Down Move
    if not outOfBoundry(boardRows, boardCols, row+1, col):
        downBoard = gc.makeMove(board, row, col, row+1, col)
        #visited[(row+1, col)] = True

        dfsRec(downBoard, row+1, col)


def dfsRec(board, row, col):
    if outOfBoundry(len(board), len(board[0]), row, col):
        return
    if board[row][col] == "1":
        return
 #   if board[row][col] == "0":
 #       gc.
 #   if walls(len(board), len(board[0]), row, col):

def outOfBoundry(rowsNumber, colsNumber, row, col):
    if (row >= rowsNumber) or (row < 0) or (col >= colsNumber) or (col < 0):
        return True

#def walls(rowsNumber, colsNumber, row, col):
   # if (row >= rowsNumber) or (row < 0) or (col >= colsNumber) or (col < 0):