from Mutation.mutation import Mutation

class NoMutation(Mutation):
    def __init__(self, probability):
        super().__init__(probability)
        

    def mutate(self, children):
        return children 