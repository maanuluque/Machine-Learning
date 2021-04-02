class NoMutation():
    def __init__(self, children_size, probability):
        self.p = probability

    def mutate(self, children):
        return children
