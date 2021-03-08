import time
from solution import Solution


def bfs(controller, node):
    current_node = node
    frontier = []
    explored = set()
    expanded = 0
    leaves = 0
    cost = 0
    start_time = time.time()

    frontier.append(current_node)  # check if deadlock?
    while len(frontier):
        current_node = frontier.pop(0)
        expanded += 1
        explored.add(hash(current_node))
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if not controller.is_deadlock(node) and hash(child) not in explored and child not in frontier:
                    child.parent = current_node
                    if controller.is_solution(child):
                        end_time = time.time()
                        processing_time = end_time - start_time
                        return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                    frontier.append(child)

    # No solution found :/
    return Solution(None, None, None, None, False, None, None)
