from Heuristics.manhattanDistance import manhattan_dist
import constants

def slb(board, boxes, player):
    if board.is_deadlock(boxes):
        return float('inf')
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
    if board.is_deadlock(boxes):
        return float('inf')
    player_dist = float('inf')
    for box in boxes:
        b = board.board
        if b[box.x][box.y] != constants.GOAL:
            aux = manhattan_dist(player, box)
            player_dist = aux if aux < player_dist else player_dist
    player_dist = 0 if player_dist == float('inf') else player_dist
    return slb(board, boxes, player) + player_dist

def slb_plus_plus(board, boxes, player):
    if board.is_deadlock(boxes):
        return float('inf')
    player_dist = float('inf')
    for box in boxes:
        b = board.board
        if b[box.x][box.y] != constants.GOAL:
            pushing_points = calculate_pushing_points(board, box)
            for point in pushing_points:
                aux = manhattan_dist(player, point)
                player_dist = aux if aux < player_dist else player_dist
    player_dist = 0 if player_dist == float('inf') else player_dist
    return slb(board, boxes, player) + player_dist

def calculate_pushing_points(board, box):
    dist = float('inf')
    for goal in board.goals:
        aux = manhattan_dist(box, goal)
        if aux < dist:
            g = goal
            dist = aux
    x = g.x - box.x
    if x == 0:
        px = box.x
        py = box.y-1 if box.y < g.y else box.y+1
        return [Point(px, py)]
    
    y = g.y - box.y
    if y == 0:
        px = box.x-1 if box.x < g.x else box.x+1
        py = box.y
        return [Point(px, py)]

    p1x = box.x-1 if box.x < g.x else box.x+1
    p1y = box.y
    p2x = box.x
    p2y = box.y-1 if box.y < g.y else box.y+1
    return [Point(p1x, p1y), Point(p2x, p2y)]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
