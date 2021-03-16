import time
from solution import Solution
from Util.queue import Queue


def bfs(controller, node):
    current_node = node
    frontier = Queue()
    exploreSet = set()
    expanded = 0
    leaves = 0
    cost = 0
    start_time = time.time()

    # Space complexity
    max_frontier_size = 1

    frontier.pushLast(current_node)  # check if deadlock?
    exploreSet.add(hash(current_node))
    while frontier.size > 0:
        current_node = frontier.popFirst()
        expanded += 1
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if hash(child) not in exploreSet:
                    child.parent = current_node
                    if controller.is_solution(child):
                        processing_time = time.time() - start_time
                        space_complexity = max_frontier_size * node.space_complexity()
                        return Solution(expanded, leaves, child, True, cost, processing_time, space_complexity)
                    frontier.pushLast(child)
                    exploreSet.add(hash(child))
            if frontier.size > max_frontier_size:
                max_frontier_size = frontier.size

    # No solution found :/
    processing_time = time.time() - start_time
    space_complexity = max_frontier_size * node.space_complexity()
    return Solution(expanded, leaves, None, False, None, processing_time, space_complexity)
