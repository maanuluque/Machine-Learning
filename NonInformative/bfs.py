
def bfs(controller, node):
    current_node = node
    frontier = []
    explored = set()
    expanded = 0
    leaves = 0
    cost = 0

    frontier.append(current_node) #check if deadlock?
    while len(frontier):
        current_node = frontier.pop()
        expanded += 1
        explored.add(current_node) #hash
        children = current_node.getChildren()
        if not children:
            leaves +=1
        else:
            for child in children:
                if not child.is_deadlock and child not in explored and child not in frontier:
                    if child.is_solution:
                        controller.moves.add(current_node)
                        return solution

