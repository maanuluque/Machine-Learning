import random

from Mutation.mutation import Mutation


class UniformMultigenMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, items_db):
        super().__init__(children_size, probability, min_h, max_h, items_db)

    def single_mutation(self, child):
        to_mutate = [*range(1, 7)]
        for i in range(0, 5):
            p = random.random()
            if p < self.probability:
                to_mutate.pop(i)
        return self.mutate_gene(child, to_mutate)

