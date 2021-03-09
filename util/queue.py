class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def push(self, node):
        if self.size == 0:
            self.first = node
            node.parent = None
        else:
            self.last.child = node
            node.parent = self.last

        node.child = None
        self.last = node
        self.size += 1

    def pop(self):
        if size == 0:
            return None
        ret = self.first
        self.first = ret.child
        self.first.parent = None
        return ret
        