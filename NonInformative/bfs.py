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
        print(f'Expanded: {expanded}')
        explored.add(hash(current_node))
        children = controller.get_children(current_node)
        print(f'Children: {len(children)}')
        if not children:
            leaves += 1
            print(f'Leaves: {leaves}')
        else:
            for child in children:
                print(f'Player current: {current_node.player.x},{current_node.player.y}')
                if not controller.is_deadlock(node) and hash(child) not in explored and child not in frontier:
                    child.parent = current_node
                    print(f'Player child: {child.player.x},{child.player.y}')
                    if controller.is_solution(child):
                        end_time = time.time()
                        processing_time = end_time - start_time
                        return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                    frontier.append(child)

    # No solution found :/
    return Solution(None, None, None, None, False, None, None)
