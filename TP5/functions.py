import numpy as np


def sigmoid_function(x):
    return 1 / (1 + np.math.exp(-2 * x))


# Assuming y = sigm(x)
def sigmoid_derivative(y):
    return 2 * y * (1 - y)


def tanh_function(x):
    return np.tanh(x)


# Assuming y = tanh(x)
def tanh_derivative(y):
    return 1 - (y ** 2)
