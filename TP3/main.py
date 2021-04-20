import numpy as np
from numpy import ndarray
from ex1.ex1_a import ex1_a
from ex1.ex1_b import ex1_b
from ex2.ex2 import ex2, ex2_stats

# print('EXERCISE 1 A:')
# ex1_a()
# print()

# print('EXERCISE 1 B:')
# ex1_b()

print('EXERCISE 2:')
training_err, testing_err = ex2(200, 3, 100)
print(f'Training error: {training_err}')
print(f'Testing  error: {testing_err}')
# ex2_stats()