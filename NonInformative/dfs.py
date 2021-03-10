import time
from solution import Solution
from Util.queue import Queue

def dfs(controller, node):
    explored = set()
    stack = Queue()
    stack_hash_values = set()
    expanded = 0
    cost = 0
    leaves = 0
    stack.pushLast(node)
    start_time = time.time()

    while stack.size > 0:
        current_node = stack.popLast()
        explored.add(hash(current_node))
        expanded += 1
        children = controller.get_children(current_node)
        if not children:
            leaves += 1
        else:
            for child in children:
                if hash(child) not in explored and hash(child) not in stack_hash_values:
                    child.parent = current_node
                    if(controller.is_solution(child)):
                        processing_time = time.time() - start_time
                        return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                    stack.pushLast(child)
                    stack_hash_values.add(hash(child))

    end_time = time.time()
    processing_time = end_time - start_time
    return Solution(expanded, leaves, explored, None, False, cost, processing_time)