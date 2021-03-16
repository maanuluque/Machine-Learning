import time
from queue import PriorityQueue
from Util.queue import Queue


from solution import Solution


def ida_star(controller, node, board, heuristic, limit):
    # Limit
    threshold = limit
    unexplored = Queue()
    unexplored_nodes = True

    # To make PQ and DFS work
    stack = Queue()
    frontier = PriorityQueue()
    reverse_frontier = Queue()

    # Initialize sizes (counters) for every queue
    stack_size = 0
    size_frontier = 0
    reverse_frontier_size = 0

    node.path_cost = 0
    explored = set()
    leaves = 0
    expanded = 0

    # Initialize
    stack.pushFirst(node)
    stack_size = stack_size + 1
    #frontier.put((node.path_cost + heuristic(board, node.boxes, node.player), node))
    #size_frontier = size_frontier + 1
    explored.add(hash(node))
    start_time = time.time()

    while unexplored_nodes:
        while stack_size > 0:
            current_node = stack.popFirst()
            stack_size = stack_size - 1
            expanded += 1
            if (current_node.path_cost + heuristic(board, current_node.boxes, current_node.player)) > threshold:
                unexplored.pushLast(current_node)
            else:
                children = controller.get_children(current_node)
                if not children:
                    leaves += 1
                else:
                    for child in children:
                        if hash(child) not in explored:
                            child.parent = current_node
                            child.path_cost = current_node.path_cost + 1
                            if controller.is_solution(child):
                                processing_time = time.time() - start_time
                                return Solution(expanded, leaves, child, True, child.path_cost, processing_time)
                            frontier.put((child.path_cost + heuristic(board, child.boxes, child.player), child))
                            size_frontier = size_frontier + 1
                            explored.add(hash(child))
                    for x in range(size_frontier):
                        reverse_frontier.pushFirst(frontier.get()[1])
                        size_frontier = size_frontier - 1
                        reverse_frontier_size = reverse_frontier_size + 1
                    for x in range(reverse_frontier_size):
                        stack.pushFirst(reverse_frontier.popFirst())
                        reverse_frontier_size = reverse_frontier_size - 1
                        stack_size = stack_size + 1
        # End Frontier while
        if unexplored.size > 0:
            unexplored_nodes = True
            threshold += limit
            iter = unexplored.size
            for x in range(0, iter):
                node = unexplored.popLast()
                frontier.put(node.path_cost + heuristic(board, node.boxes, node.player), node)
        else:
            unexplored_nodes = False

    processing_time = time.time() - start_time
    return Solution(expanded, leaves, None, False, 0, processing_time)
