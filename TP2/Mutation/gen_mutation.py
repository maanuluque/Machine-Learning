from Mutation.mutation import Mutation
import random


class GenMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, items_db):
        super().__init__(children_size, probability, min_h, max_h, items_db)

    def single_mutation(self, child):
        gene = random.randint(1, 6)
        p = random.random()
        print(f'Gene: {gene}, Prob: {p}')
        if p < self.probability:
            return child
        return self.mutate_gene(child, [gene])

