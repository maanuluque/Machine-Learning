from munkres import Munkres
from Heuristics.manhattanDistance import manhattan_dist


def mmlb(board, boxes, player):
    if board.is_deadlock(boxes):
        return float('inf')
    dim = len(boxes)
    goals = board.goals
    matrix = [['0' for _ in range(dim)] for _ in range(dim)]

    for x, box in enumerate(boxes):
        for y, goal in enumerate(goals):
            matrix[x][y] = manhattan_dist(box, goal)

    m = Munkres()
    indexes = m.compute(matrix)
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total += value
    return total
