from Heuristics.manhattanDistance import manhattan_dist


def slb(board, boxes, player):
    total_sum = 0
    dist = 0
    for box in boxes:
        for goal in board.goals:
            aux = manhattan_dist(box, goal)
            dist = aux if dist == 0 or aux < dist else dist
        total_sum = total_sum + dist
        dist = 0
    return total_sum

def slb_plus(board, boxes, player):
    pass
