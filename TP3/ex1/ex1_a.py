import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy as cp
from perceptron.simpleperceptron import SimplePerceptron

def ex1_a():
    w = [0, 0, 0]
    train_list = [
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1]
    ]
    expected_list = [
        -1,
        -1,
        -1,
        1,
    ]

    print('LOGICAL AND')
    sp = SimplePerceptron(w, 0.2)
    print('Initial Perceptron:')
    print(sp)
    print('Initial predictions:')
    print(f'-1  1 : {sp.predict([1, -1, 1])}')
    print(f' 1 -1 : {sp.predict([1, 1, -1])}')
    print(f'-1 -1 : {sp.predict([1, -1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1, 1])}')
    w_last = cp(sp.weights)
    max_iter = 100
    i = 0
    while i < max_iter:
        sp.train_list(train_list, expected_list)
        if w_last == sp.weights:
            print(f'\nConverged at iter {i}\n')
            break
        w_last = cp(sp.weights)
        i += 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final Perceptron:')
    print(sp)
    print('Final predictions:')
    print(f'-1  1 : {sp.predict([1, -1, 1])}')
    print(f' 1 -1 : {sp.predict([1, 1, -1])}')
    print(f'-1 -1 : {sp.predict([1, -1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1, 1])}')

    # Plot

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
    m = -sp.weights[1] / sp.weights[2]
    b = -sp.weights[0] / sp.weights[2]
    ax.plot(x, m * x + b)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('AND logical function')
    plt.plot()
    plt.show()
