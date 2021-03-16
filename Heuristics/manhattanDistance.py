def manhattan_dist(box, goal):
    return abs(box.x - goal.x) + abs(box.y - goal.y)
