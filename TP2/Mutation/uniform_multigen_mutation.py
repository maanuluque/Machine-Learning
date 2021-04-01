from Mutation.mutation import Mutation


class UniformMultigenMutation(Mutation):
    def __init__(self, children_size, probability):
        super().__init__(children_size, probability)

    def single_mutation(self):
        pass

    def mutate(self, children):
        return children
