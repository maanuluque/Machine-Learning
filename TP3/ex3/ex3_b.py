import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray
from perceptron.multiperceptron import MultiPerceptron
from random import randint
from math import copysign


# Functions
def step_function(x):
    return copysign(1, x)


def linear_function(x):
    return x


def tanh_function(x):
    return np.tanh(x)


def sigmoid_function(x):
    return 1 / (1 + np.exp(-2 * x))


# Derivatives
def step_derivative(x):
    return 1


def linear_derivative(x):
    return np.array([1 for _ in x])


# Assuming y = tanh(x)
def tanh_derivative(y):
    return 1 - (y ** 2)


# Assuming y = sigm(x)
def sigmoid_derivative(y):
    return 2 * y * (1 - y)


def transfer_deriv(y):
    return y * (1 - y)


def ex3_b():
    data_max = 70
    data_cols = 5

    data_list = list()
    expected_gen: list = [[-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1]]
    expected_list: ndarray = np.array(expected_gen)
    bias: float = 1
    with open('ex3/ex3-pixel-digit-decimal-map.txt') as f:
        digit = -1
        for r, line in enumerate(f):
            if r == data_max:
                break
            data = line.split()
            if (r % 7) == 0:
                data_list.append([bias])
                digit += 1
            for c in range(0, data_cols):
                data_list[digit].append(float(data[c]))

    mp = MultiPerceptron(tanh_function, tanh_derivative, learning_rate=0.1,
                         beta=1, layers=3, layer_dims=[2, 3, 1], data_dim=36)

    for _ in range(0, 100000):
        idx = randint(0, 9)
        mp.train(data_list[idx], expected_list[idx])
    # delta = 0.1
    # good = 0
    # bad = 0
    # epochs = list()
    # accuracy = list()
    # for epoch in range(0, 500):
    #     for idx in range(0, 7):
    #         mp.train(data_list[idx], expected_list[idx])
    #     for idx in range(0, 7):
    #         prediction = mp.predict(data_list[idx])
    #         if abs(expected_list[idx] - prediction) < delta:
    #             good += 1
    #         else:
    #             bad += 1
    #     epochs.append(epoch)
    #     accuracy.append(good/7)
    #     good = 0
    #     bad = 0

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final predictions:')
    print('Perceptron:')
    print(f' 0 : {mp.predict(data_list[0])}')
    print(f' 1 : {mp.predict(data_list[1])}')
    print(f' 2 : {mp.predict(data_list[2])}')
    print(f' 3 : {mp.predict(data_list[3])}')
    print(f' 4 : {mp.predict(data_list[4])}')
    print(f' 5 : {mp.predict(data_list[5])}')
    print(f' 6 : {mp.predict(data_list[6])}')
    print(f' 7 : {mp.predict(data_list[7])}')
    print(f' 8 : {mp.predict(data_list[8])}')
    print(f' 9 : {mp.predict(data_list[9])}')