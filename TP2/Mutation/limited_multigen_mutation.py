import random
from Mutation.mutation import Mutation


class LimitedMultigenMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, items_db):
        super().__init__(children_size, probability, min_h, max_h, items_db)

    def single_mutation(self, child):
        mutations_quantity = random.randint(1, 6)
        to_mutate = []
        while mutations_quantity > 0:
            mutate_gene = random.randint(1, 6)
            if mutate_gene not in to_mutate:
                to_mutate.append(mutate_gene)
                mutations_quantity = mutations_quantity - 1
        for i in range(0, 5):
            p = random.random()
            if p < self.probability:
                to_mutate.pop(i)
        return self.mutate_gene(child, to_mutate)
