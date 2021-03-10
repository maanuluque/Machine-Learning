class Solution:

    def __init__(self, expanded, leaves, path, solved, cost, processing_time):
        self.expanded = expanded
        self.leaves = leaves
        self.solved = solved
        self.cost = cost
        self.processing_time = processing_time
        self.depth = 0

        current_node = path
        while hasattr(current_node, 'parent'):
            self.depth += 1
            child = current_node
            current_node = current_node.parent
            current_node.child = child
        self.path = current_node

