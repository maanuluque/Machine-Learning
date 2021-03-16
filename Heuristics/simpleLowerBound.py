from Heuristics.manhattanDistance import manhattan_dist


def slb(board, boxes, player):
    total_sum = 0
    dist = float('inf')
    for box in boxes:
        for goal in board.goals:
            aux = manhattan_dist(box, goal)
            dist = aux if aux < dist else dist
        total_sum = total_sum + dist
        dist = 0
    return total_sum


def slb_plus(board, boxes, player):
    player_dist = float('inf')
    for box in boxes:
        aux = manhattan_dist(player, box)
        player_dist = aux if aux < player_dist else player_dist
    return slb(board, boxes, player) + player_dist
