from sortedcontainers import SortedList

class SortedListAdapter(SortedList):
    def append(self, x):
        return self.add(x)

    def extend(self, x):
        return self.update(x)