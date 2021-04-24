from perceptron.multiperceptron import MultiPerceptron
from matplotlib import pyplot as plt
from copy import deepcopy as cp
from math import copysign
from random import randint
import numpy as np

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
    return 1 - (y**2)

# Assuming y = sigm(x)
def sigmoid_derivative(y):
    return 2 * y * (1 - y)

def transfer_deriv(y):
    return y * (1 - y)

def ex3_a():
    mp = MultiPerceptron(tanh_function, tanh_derivative, learning_rate=0.1, 
                        beta=1, layers=3, layer_dims=[3, 3, 1], data_dim=3)

    data = np.array([[1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1]])
    expected = np.array([[-1], [-1], [1], [1]])

    for _ in range(0, 100000):
        idx = randint(0, 3)
        mp.train(data[idx], expected[idx])

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final predictions:')
    print('Perceptron:')
    print(mp)
    print(f' 1  1 : {mp.predict(data[0])}')
    print(f'-1 -1 : {mp.predict(data[1])}')
    print(f'-1  1 : {mp.predict(data[2])}')
    print(f' 1 -1 : {mp.predict(data[3])}')