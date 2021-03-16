import time
from solution import Solution
from Util.queue import Queue

def iddfs(controller, node, limit):
    threshold = limit
    explored = set()
    unexplored = Queue()
    stack = Queue()
    unexplored_nodes = True
    expanded = 0
    cost = 0
    leaves = 0
    current_depth = 0
    node.depth = current_depth
    stack.pushLast(node)
    explored.add(hash(node))

    # Space complexity
    max_stack_size = 1

    start_time = time.time()

    while unexplored_nodes:
        while stack.size > 0:
            current_node = stack.popLast()
            current_depth = current_node.depth
            if current_depth < threshold:
                expanded += 1
                children = controller.get_children(current_node)
                if children:
                    current_depth += 1
                    for child in children:
                        if hash(child) not in explored:
                            child.depth = current_depth
                            child.parent = current_node
                            if (controller.is_solution(child)):
                                processing_time = time.time() - start_time
                                space_complexity = node.space_complexity() * max_stack_size
                                return Solution(expanded, leaves, child, True, cost, processing_time, space_complexity)
                            stack.pushLast(child)
                            explored.add(hash(child))
                    if stack.size > max_stack_size:
                        max_stack_size = stack.size
                else:
                    leaves += 1
            else:
                unexplored.pushLast(current_node)
        # End Stack while
        if unexplored.size > 0:
            unexplored_nodes = True
            threshold += limit
            iter = unexplored.size
            for x in range(0, iter):
                stack.pushLast(unexplored.popLast())
        else:
            unexplored_nodes = False

    space_complexity = node.space_complexity() * max_stack_size
    processing_time = time.time() - start_time
    return Solution(expanded, leaves, None, False, cost, processing_time, space_complexity)