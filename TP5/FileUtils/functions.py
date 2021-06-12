import numpy as np
from scipy.optimize import minimize


def sigmoid_function(x):
    for i in range(x.shape[0]):
        x[i] = 1 / (1 + np.math.exp(-2 * x[i]))
    return x

def sigmoid_scalar_function(x):
    return 1 / (1 + np.math.exp(-2 * x))

def opt_sigmoid_function(x):
    for i in range(x.shape[0]):
        res = minimize(sigmoid_scalar_function, x, method='powell')
        x[i] = res.x
    return x


# def sigmoid_function(x):
#     return  1 / (1 + np.math.exp(-2 * x))

# Assuming y = sigm(x)
def sigmoid_derivative(y):
    return 2 * y * (1 - y)


def tanh_function(x):
    return np.tanh(x)


# Assuming y = tanh(x)
def tanh_derivative(y):
    return 1 - (y ** 2)


def min_tanh(x):
    return minimize(tanh_function, x, method='powell')


def relu(x):
    return max(0, x)


def relu_derivative(x):
    if x > 0:
        return 1
    return 0
