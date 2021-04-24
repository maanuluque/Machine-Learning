import numpy as np
from numpy import ndarray
from matplotlib import pyplot as plt
from copy import deepcopy as cp
from math import copysign
from perceptron.multiperceptron import MultiPerceptron

# Functions
def step_function(x):
    return copysign(1, x)

# Derivatives
def step_derivative(x):
    return 1

def ex1_a():
    train_list: ndarray = np.array([
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1]
    ], dtype=float)
    expected_list: ndarray = np.array([
        [-1],
        [-1],
        [-1],
        [1],
    ], dtype=float)

    print('LOGICAL AND')
    mp = MultiPerceptron(step_function, step_derivative, learning_rate=0.2, beta=1, layers=1, layer_dims=[1], data_dim=3)
    print('Initial Perceptron:')
    print(mp)
    print('Initial predictions:')
    print(f'-1  1 : {mp.predict(np.array([1, -1,  1]))}')
    print(f' 1 -1 : {mp.predict(np.array([1,  1, -1]))}')
    print(f'-1 -1 : {mp.predict(np.array([1, -1, -1]))}')
    print(f' 1  1 : {mp.predict(np.array([1,  1,  1]))}')
    max_iter = 10000
    i = 0
    while i < max_iter:
        mp.train_list(train_list, expected_list)
        i += 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final Perceptron:')
    print(mp)
    print('Final predictions:')
    print(f'-1  1 : {mp.predict(np.array([1, -1,  1]))}')
    print(f' 1 -1 : {mp.predict(np.array([1,  1, -1]))}')
    print(f'-1 -1 : {mp.predict(np.array([1, -1, -1]))}')
    print(f' 1  1 : {mp.predict(np.array([1,  1,  1]))}')

    # Plot

    weights = mp.layers[0].weights[0]

    fig, ax = plt.subplots()
    x_min, x_max = -2, 2
    x = np.arange(x_min, x_max, 0.1)
    for idx, point in enumerate(train_list):
        if expected_list[idx] == 1:
            ax.scatter(point[1], point[2], color="b")
        if expected_list[idx] == -1:
            ax.scatter(point[1], point[2], color="r")
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([-2, 2])
    m = -weights[1] / weights[2]
    b = -weights[0] / weights[2]
    ax.plot(x, m * x + b)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('AND logical function')
    plt.plot()
    plt.show()
