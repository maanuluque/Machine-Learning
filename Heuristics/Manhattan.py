def manhattan(board, boxes):
    total_sum = 0
    dist = 0
    for box in boxes:
        for goal in board.goals:
            aux = manhattan_dist(box, goal)
            dist = aux if dist == 0 or aux < dist else dist
        total_sum = total_sum + dist
        dist = 0
    return total_sum


def manhattan_dist(box, goal):
    return abs(box.x - goal.x) + abs(box.y - goal.y)
