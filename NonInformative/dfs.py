import time
from solution import Solution

def dfs(controller, node):
    explored = set()
    stack = []
    expanded = 0
    cost = 0
    leaves = 0
    stack.append(node)
    start_time = time.time()

    while stack:
        current_node = stack.pop()
        explored.add(hash(current_node))
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if not controller.is_deadlock(child) and hash(child) not in explored and child not in stack:
                    child.parent = current_node
                    if(controller.is_solution(child)):
                        end_time = time.time()
                        processing_time = end_time - start_time
                        return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                    stack.append(child)

    return Solution(None, None, None, None, False, None, None)