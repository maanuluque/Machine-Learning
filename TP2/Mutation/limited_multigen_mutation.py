import random
from Mutation.mutation import Mutation


class LimitedMultigenMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, height_decimals, items_db):
        super().__init__(children_size, probability, min_h, max_h, height_decimals, items_db)

    def single_mutation(self, child):
        mutations_quantity = random.randint(1, 6)
        to_mutate = []
        size = 6
        while mutations_quantity > 0:
            rand_idx = random.randint(0, size-1)
            mutate_gene = self.genes_idx.pop(rand_idx)
            self.aux_idx.append(mutate_gene)
            size -= 1
            to_mutate.append(mutate_gene)
            mutations_quantity = mutations_quantity - 1
        self.genes_idx.extend(self.aux_idx)
        self.aux_idx = []

        mutate = []
        for gene in to_mutate:
            p = random.random()
            if p >= self.probability:
                mutate.append(gene)
        return self.mutate_gene(child, mutate)
