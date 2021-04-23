from math import copysign
import numpy as np

# Functions
def step_function(x):
    return copysign(1, x)

def linear_function(x):
    return x

def tanh_function(x):
    return np.math.tanh(x)

def sigmoid_function(x):
    return 1 / (1 + np.math.exp(-2 * x))

# Derivatives
def step_derivative(x):
    return 1

def linear_derivative(x):
    return 1

# Assuming y = tanh(x)
def tanh_derivative(y):
    return 1 - (y**2)

# Assuming y = sigm(x)
def sigmoid_derivative(y):
    return 2 * y * (1 - y)