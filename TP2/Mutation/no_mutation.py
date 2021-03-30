from Mutation.mutation import Mutation

class NoMutation(Mutation):
    def __init__(self, children_size, probability):
        super().__init__(children_size, probability)
        

    def mutate(self, children):
        return children 