import time
from solution import Solution
from Util.queue import Queue


def bfs(controller, node):
    current_node = node
    frontier = Queue()
    frontierSet = set()
    explored = set()
    expanded = 0
    leaves = 0
    cost = 0
    start_time = time.time()

    frontier.pushLast(current_node)  # check if deadlock?
    while frontier.size > 0:
        current_node = frontier.popFirst()
        # frontierSet.discard(hash(current_node)) # TODO worth?
        expanded += 1
        explored.add(hash(current_node))
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if hash(child) not in explored and hash(child) not in frontierSet:
                    child.parent = current_node
                    if controller.is_solution(child):
                        processing_time = time.time() - start_time
                        return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                    frontier.pushLast(child)
                    frontierSet.add(hash(child))

    # No solution found :/
    processing_time = time.time() - start_time
    return Solution(expanded, leaves, explored, None, False, None, processing_time)
