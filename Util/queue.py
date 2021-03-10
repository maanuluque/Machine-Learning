class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def pushLast(self, data):
        node = self.Node(data)
        if self.size == 0:
            self.first = node
        else:
            self.last.child = node

        node.parent = self.last
        node.child = None
        self.last = node
        self.size += 1

    def pushFirst(self, data):
        node = self.Node(data)
        if self.size == 0:
            self.last = node
        else:
            self.first.parent = node

        node.child = self.first
        node.parent = None
        self.first = node
        self.size += 1

    def popFirst(self):
        if self.size == 0:
            return None
        ret = self.first
        self.first = ret.child
        if self.first != None:
            self.first.parent = None
        self.size -= 1
        return ret.data

    def popLast(self):
        if self.size == 0:
            return None
        ret = self.last
        self.last = ret.parent
        if self.last != None:
            self.last.child = None
        self.size -= 1
        return ret.data

    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = None
            self.child = None
        