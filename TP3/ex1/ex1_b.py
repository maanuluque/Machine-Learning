import numpy as np
from numpy import ndarray
from perceptron.multiperceptron import MultiPerceptron
from math import copysign

# Functions
def step_function(x):
    return copysign(1, x)

# Derivatives
def step_derivative(x):
    return 1

def ex1_b():
    train_list: ndarray = np.array([
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1]
    ], dtype=float)
    expected_list: ndarray = np.array([
        [1],
        [1],
        [-1],
        [-1],
    ], dtype=float)

    print('LOGICAL XOR:')
    mp = MultiPerceptron(step_function, step_derivative, learning_rate=0.2, beta=1, layers=1, layer_dims=[1], data_dim=3)
    print('Initial Perceptron:')
    print(mp)
    print('Initial predictions:')
    print(f'-1  1 : {mp.predict(np.array([1, -1,  1]))}')
    print(f' 1 -1 : {mp.predict(np.array([1,  1, -1]))}')
    print(f'-1 -1 : {mp.predict(np.array([1, -1, -1]))}')
    print(f' 1  1 : {mp.predict(np.array([1,  1,  1]))}')

    times = 1000
    while times:
        mp.train_list(train_list, expected_list)
        times -= 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final predictions:')
    print('Perceptron:')
    print(mp)
    print(f'-1  1 : {mp.predict(np.array([1, -1,  1]))}')
    print(f' 1 -1 : {mp.predict(np.array([1,  1, -1]))}')
    print(f'-1 -1 : {mp.predict(np.array([1, -1, -1]))}')
    print(f' 1  1 : {mp.predict(np.array([1,  1,  1]))}')