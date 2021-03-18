import time
from queue import PriorityQueue
from Util.queue import Queue
from solution import Solution


def ida_star(controller, node, board, heuristic):
    # Limit
    h = heuristic(board, node.boxes, node.player)
    threshold = h

    # To make PQ and DFS work
    stack = Queue()
    frontier = PriorityQueue()

    explored = set()
    expanded = 0

    # Initialize
    node.path_cost = 0
    frontier.put((h, node))
    frontier_size = 1
    explored.add(hash(node))
    start_time = time.time()

    # Space complexity
    max_frontier_size = 1

    while frontier_size > 0 or stack.size > 0:
        while stack.size > 0:
            current_node = stack.popFirst()
            sol = controller.is_solution(current_node)
            if sol:
                space_complexity = (max_frontier_size + current_node.path_cost)*node.space_complexity()
                processing_time = time.time() - start_time
                current_size = stack.size + frontier_size
                return Solution(expanded, current_size, current_node, True, current_node.path_cost, processing_time, space_complexity)
            expanded += 1
            children = controller.get_children(current_node)
            if children:
                for child in children:
                    if hash(child) not in explored:
                        child.parent = current_node
                        child.path_cost = current_node.path_cost + 1
                        h = heuristic(board, child.boxes, child.player)
                        f = child.path_cost + h
                        if f > threshold:
                            frontier.put((f, child))
                            frontier_size += 1
                            explored.add(hash(child))
                        else:
                            stack.pushLast(child)
                            explored.add(hash(child))
                        current_size = stack.size + frontier_size
                        if current_size > max_frontier_size:
                                max_frontier_size = current_size

        # End Frontier while
        if frontier_size > 0:
            stack.pushLast(frontier.get()[1])  
            frontier_size -= 1

    space_complexity = (max_frontier_size) * node.space_complexity()
    processing_time = time.time() - start_time
    return Solution(expanded, 0, None, False, 0, processing_time, space_complexity)
