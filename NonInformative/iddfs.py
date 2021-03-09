import time
from solution import Solution

def iddfs(controller, node, limit):
    explored = set()
    stack = []
    unexplored = []
    unexplored_nodes = True
    expanded = 0
    cost = 0
    leaves = 0
    current_depth = 0
    node.depth = current_depth
    stack.append(node)

    start_time = time.time()

    while unexplored_nodes:
        while stack:
            current_node = stack.pop()
            current_depth = current_node.depth
            explored.add(hash(current_node))
            if current_depth < limit:
                children = controller.get_children(current_node)
                if children:
                    current_depth += 1
                    for child in children:
                        child.depth = current_depth
                        if not controller.is_deadlock(child) and hash(child) not in explored and child not in stack:
                            child.parent = current_node
                            if (controller.is_solution(child)):
                                end_time = time.time()
                                processing_time = end_time - start_time
                                return Solution(expanded, leaves, explored, child, True, cost, processing_time)
                            stack.append(child)
                else:
                    unexplored.append(current_node)
                    leaves += 1
        # End Stack while
        if unexplored:
            unexplored_nodes = True
            limit = limit/2
            iter = len(unexplored)
            for x in range(0, iter):
                stack.append(unexplored.pop())
        else:
            unexplored_nodes = False


    return Solution(None, None, None, None, False, None, None)