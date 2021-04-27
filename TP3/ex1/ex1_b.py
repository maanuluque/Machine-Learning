import numpy as np
from numpy import ndarray
from perceptron.multiperceptron import MultiPerceptron
from math import copysign
from matplotlib import pyplot as plt


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

def ex1_b_2():
    train_list: ndarray = np.array([
        [1, -1,  1, (-1* 1)],
        [1,  1, -1, ( 1*-1)],
        [1, -1, -1, (-1*-1)],
        [1,  1,  1, ( 1* 1)]
    ], dtype=float)
    expected_list: ndarray = np.array([
        [1],
        [1],
        [-1],
        [-1],
    ], dtype=float)

    print(train_list)
    print('LOGICAL XOR KERNEL:')
    mp = MultiPerceptron(step_function, step_derivative, learning_rate=0.2, beta=1, layers=1, layer_dims=[1], data_dim=4)
    print('Initial Perceptron:')
    print(mp)
    print('Initial predictions:')
    print(f'-1  1 : {mp.predict(train_list[0])}')
    print(f' 1 -1 : {mp.predict(train_list[1])}')
    print(f'-1 -1 : {mp.predict(train_list[2])}')
    print(f' 1  1 : {mp.predict(train_list[3])}')

    times = 1000
    while times:
        mp.train_list(train_list, expected_list)
        times -= 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final predictions:')
    print('Perceptron:')
    print(mp)
    print(f'-1  1 : {mp.predict(train_list[0])}')
    print(f' 1 -1 : {mp.predict(train_list[1])}')
    print(f'-1 -1 : {mp.predict(train_list[2])}')
    print(f' 1  1 : {mp.predict(train_list[3])}')

    # Plot

    weights = mp.layers[0].weights[0]

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    x_min, x_max = -3, 3
    y_min, y_max = -3, 3
    z_min, z_max = -3, 3
    x = np.arange(x_min, x_max, 0.1)
    y = np.arange(y_min, y_max, 0.1)
    for idx, point in enumerate(train_list):
        if expected_list[idx] == 1:
            ax.scatter(point[1], point[2], point[3], color="b")
        if expected_list[idx] == -1:
            ax.scatter(point[1], point[2], point[3], color="r")
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.set_zlim([z_min, z_max])
    m1 = -weights[1] / weights[3]
    m2 = -weights[2] / weights[3]
    b = -weights[0] / weights[3]
    z = lambda x,y: (m1 * x) + (m2 * y) + b

    X = np.array([x, x, x, x, x, x, x])
    Y = np.array([y-3, y-2, y-1, y, y+1, y+2, y+3])
    Z = np.array([z(x-3,y-3), z(x-2,y-2), z(x-1,y-1), z(x,y), z(x+1,y+1), z(x+2,y+2), z(x+3,y+3)])

    ax.plot_surface(X,Y,Z, color='skyblue')

    plt.title('XOR logical function')
    plt.show()