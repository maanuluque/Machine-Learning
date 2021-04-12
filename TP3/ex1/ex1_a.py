import numpy as np
from matplotlib import pyplot as plt

from perceptron.simpleperceptron import SimplePerceptron

def ex1_a():
    w = [-1, 1]
    train_list = [
        [-1, 1],
        [1, -1],
        [-1, -1],
        [1, 1]
    ]
    expected_list = [
        -1,
        -1,
        -1,
        1,
    ]

    print('LOGICAL AND')
    sp = SimplePerceptron(w, 0.3, 0.1)
    print('Initial Perceptron:')
    print(sp)
    print('Initial predictions:')
    print(f'-1  1 : {sp.predict([-1, 1])}')
    print(f' 1 -1 : {sp.predict([1, -1])}')
    print(f'-1 -1 : {sp.predict([-1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1])}')
    i = 100000
    while i > 0:
        sp.train_list(train_list, expected_list)
        i -= 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final Perceptron:')
    print(sp)
    print('Final predictions:')
    print(f'-1  1 : {sp.predict([-1, 1])}')
    print(f' 1 -1 : {sp.predict([1, -1])}')
    print(f'-1 -1 : {sp.predict([-1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1])}')

    # Plot

    fig, ax = plt.subplots()
    x_min, x_max = -2, 2
    x = np.arange(x_min, x_max, 0.1)
    y = [1] * len(x)
    for idx, point in enumerate(train_list):
        if expected_list[idx] == 1:
            ax.scatter(point[0], point[1], color="b")
        if expected_list[idx] == -1:
            ax.scatter(point[0], point[1], color="r")
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([-2, 2])
    m = -sp.weights[0] / sp.weights[1]
    b = sp.threshold / sp.weights[1]
    print(f'M: {m} B: {b}')
    # print(m, c)
    ax.plot(x, m * x + b)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('AND logical function')
    plt.plot()
    plt.show()
