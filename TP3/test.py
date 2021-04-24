import numpy as np
import random
from numpy import ndarray
from ex1.ex1_a import ex1_a
from ex1.ex1_b import ex1_b
from ex2.ex2 import ex2, ex2_stats

# print('EXERCISE 1 A:')
# ex1_a()
# print()

# print('EXERCISE 1 B:')
# ex1_b()

# print('EXERCISE 2:')
# training_err, testing_err = ex2(200, 3, 100)
# print(f'Training error: {training_err}')
# print(f'Testing  error: {testing_err}')
# ex2_stats()

from perceptron.multiperceptron import MultiPerceptron
from perceptron.simpleperceptron import SimplePerceptron
from matplotlib import pyplot as plt
from copy import deepcopy as cp

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

print('Testing multilayer :/')
mp = MultiPerceptron(tanh_function, tanh_derivative, learning_rate=0.1, 
                    beta=1, layers=3, layer_dims=[2, 3, 1], data_dim=3)

data = np.array([[1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1]])
expected = np.array([[-1], [-1], [1], [1]])

for _ in range(0, 100000):
    idx = random.randint(0, 3)
    mp.train(data[idx], expected[idx])

print(mp)
print(mp.predict(data[0]))
print(mp.predict(data[1]))
print(mp.predict(data[2]))
print(mp.predict(data[3]))

# w = mp.layers[0].weights
# print(w)

# fig, ax = plt.subplots()
# x_min, x_max = -3, 3
# x = np.arange(x_min, x_max, 0.1)
# for idx, point in enumerate(data):
#     if expected[idx] == 1:
#         ax.scatter(point[1], point[2], color="b")
#     if expected[idx] == -1:
#         ax.scatter(point[1], point[2], color="r")
# ax.set_xlim([x_min, x_max])
# ax.set_ylim([-3, 3])

# m = -w[0][1] / w[0][2]
# b = -w[0][0] / w[0][2]
# ax.plot(x, m * x + b)

# m2 = -w[1][1] / w[1][2]
# b2 = -w[1][0] / w[1][2]
# ax.plot(x, m2 * x + b2)

# plt.xlabel('X1')
# plt.ylabel('X2')
# plt.title('XOR logical function')
# plt.plot()
# plt.show()