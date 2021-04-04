import random
from Mutation.mutation import Mutation


class UniformMultigenMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, height_decimals, items_db):
        super().__init__(children_size, probability, min_h, max_h, items_db)
        self.to_mutate = [*range(1, 7)]

    def single_mutation(self, child):
        mutate = []
        for i in self.to_mutate:
            p = random.random()
            if p < self.probability:
                mutate.append(i)
        return self.mutate_gene(child, mutate)

