import time
from solution import Solution
from Util.queue import Queue

def iddfs(controller, node, limit):
    threshold = limit
    explored = {}
    unexplored = Queue()
    stack = Queue()
    unexplored_nodes = True
    expanded = 0
    cost = 0
    leaves = 0
    current_depth = 0
    node.depth = current_depth
    stack.pushLast(node)
    explored[hash(node)] = node.depth

    # Space complexity
    max_stack_size = 1

    start_time = time.time()

    while unexplored_nodes:
        while stack.size > 0:
            current_node = stack.popLast()
            current_depth = current_node.depth
            if (controller.is_solution(current_node)):
                leaves = stack.size
                processing_time = time.time() - start_time
                space_complexity = current_node.space_complexity() * max_stack_size
                return Solution(expanded, leaves, current_node, True, cost, processing_time, space_complexity)
            if current_depth < threshold:
                expanded += 1
                children = controller.get_children(current_node)
                if children:
                    current_depth += 1
                    for child in children:
                        child.depth = current_depth
                        hash_child = hash(child) 
                        if hash_child not in explored or explored[hash_child] > child.depth:
                            child.parent = current_node
                            stack.pushLast(child)
                            explored[hash(child)] = child.depth
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
            aux = stack
            stack = unexplored
            unexplored = aux
            # iter = unexplored.size
            # for x in range(0, iter):
            #     stack.pushLast(unexplored.popLast())
        else:
            unexplored_nodes = False

    leaves = 0
    space_complexity = node.space_complexity() * max_stack_size
    processing_time = time.time() - start_time
    return Solution(expanded, leaves, None, False, cost, processing_time, space_complexity)