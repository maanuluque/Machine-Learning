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
        if expanded % 100 == 0:
            print(f'{time.time() - start_time} - poping....')
        current_node = frontier.pop(0)
        if expanded % 100 == 0:
            print(f'{time.time() - start_time} - POP')
        expanded += 1
        hsh = hash(current_node)
        if expanded % 100 == 0:
            print(f'{time.time() - start_time} - HASH')
        explored.add(hsh)
        if expanded % 100 == 0:
            print(f'{time.time() - start_time} - Add')
        children = controller.get_children(current_node)
        if expanded % 100 == 0:
            print(f'{time.time() - start_time} - Children')
        if not children:
            leaves += 1
        else:
            for child in children:
                if hash(child) not in explored and child not in frontier:
                    child.parent = current_node
                    if controller.is_solution(child):
                        processing_time = time.time() - start_time
                        return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                    frontier.append(child)

    # No solution found :/
    processing_time = time.time() - start_time
    return Solution(expanded, leaves, explored, None, False, None, processing_time)
