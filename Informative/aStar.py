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
    frontier.put((node.path_cost + heuristic(board, node.boxes, node.player), node))
    size_frontier = size_frontier + 1
    explored.add(hash(node))
    start_time = time.time()

    # Space complexity
    max_frontier_size = size_frontier

    while size_frontier > 0:
        current_node = frontier.get()[1]
        size_frontier = size_frontier - 1
        expanded += 1
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if hash(child) not in explored:
                    child.parent = current_node
                    child.path_cost = current_node.path_cost + 1
                    if controller.is_solution(child):
                        leaves = size_frontier
                        processing_time = time.time() - start_time
                        space_complexity = max_frontier_size * node.space_complexity()
                        return Solution(expanded, leaves, child, True, child.path_cost, processing_time, space_complexity)
                    frontier.put((child.path_cost + heuristic(board, child.boxes, child.player), child))

                    size_frontier = size_frontier + 1
                    explored.add(hash(child))
            if size_frontier > max_frontier_size:
                max_frontier_size = size_frontier

    leaves = 0
    space_complexity = max_frontier_size * node.space_complexity()
    processing_time = time.time() - start_time
    return Solution(expanded, leaves, None, False, 0, processing_time, space_complexity)
