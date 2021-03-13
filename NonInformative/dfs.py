import time
from solution import Solution
from Util.queue import Queue

def dfs(controller, node):
    explored = set()
    stack = Queue()
    expanded = 0
    cost = 0
    leaves = 0
    stack.pushLast(node)
    explored.add(hash(node))
    start_time = time.time()

    while stack.size > 0:
        current_node = stack.popLast()
        expanded += 1
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if hash(child) not in explored:
                    child.parent = current_node
                    if(controller.is_solution(child)):
                        processing_time = time.time() - start_time
                        return Solution(expanded, leaves, child, True, cost, processing_time)
                    stack.pushLast(child)
                    explored.add(hash(child))

    processing_time = time.time() - start_time
    return Solution(expanded, leaves, None, False, cost, processing_time)
