from Mutation.mutation import Mutation


class LimitedMultigenMutation(Mutation):
    def __init__(self, children_size, probability, min_h, max_h, items_db):
        super().__init__(children_size, probability, min_h, max_h, items_db)

    def single_mutation(self, child):
        pass


