import time
from queue import PriorityQueue
from solution import Solution


def a_star(controller, node, board, heuristic):
    node.path_cost = 0
    size_frontier = 0
    frontier = PriorityQueue()
    explored = set()
    expanded = 0
    leaves = 0
    wrp = AStarWrapper(node.path_cost, heuristic(board, node.boxes, node.player), node)
    frontier.put(wrp)
    size_frontier = size_frontier + 1
    explored.add(hash((node.path_cost, node)))
    start_time = time.time()

    # Space complexity
    max_frontier_size = size_frontier

    while size_frontier > 0:
        current_node = frontier.get().node
        size_frontier = size_frontier - 1
        if controller.is_solution(current_node):
            leaves = size_frontier
            processing_time = time.time() - start_time
            space_complexity = max_frontier_size * node.space_complexity()
            return Solution(expanded, leaves, current_node, True, current_node.path_cost, processing_time, space_complexity)
        children = controller.get_children(current_node)
        expanded += 1
        if not children:
            leaves += 1
        else:
            for child in children:
                child.path_cost = current_node.path_cost + 1
                if hash((child.path_cost, child)) not in explored:
                    child.parent = current_node
                    wrp = AStarWrapper(child.path_cost, heuristic(board, child.boxes, child.player), child)
                    frontier.put(wrp)
                    size_frontier = size_frontier + 1
                    explored.add(hash((child.path_cost, child)))
            if size_frontier > max_frontier_size:
                max_frontier_size = size_frontier

    leaves = 0
    space_complexity = max_frontier_size * node.space_complexity()
    processing_time = time.time() - start_time
    return Solution(expanded, leaves, None, False, 0, processing_time, space_complexity)

class AStarWrapper:
    def __init__(self, g, h, node):
        self.g = g
        self.h = h
        self.node = node

    def __hash__(self):
        return hash((self.g, hash(self.node)))

    def __eq__(self, other):
        if not self.g == other.g or not self.node == other.node:
            return False
        return True

    def __lt__(self, other):
        comp = self.g + self.h - other.g - other.h
        if comp != 0:
            return comp < 0
        return self.h < other.h