import numpy as np
from numpy import ndarray
from perceptron.simpleperceptron import SimplePerceptron

def ex1_b():
    w: ndarray = np.array([0, 0, 0], dtype=float)
    train_list: ndarray = np.array([
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1]
    ], dtype=float)
    expected_list: ndarray = np.array([
        1,
        1,
        -1,
        -1,
    ], dtype=float)

    print('LOGICAL XOR:')
    sp = SimplePerceptron(w, 0.1)
    print('Initial Perceptron:')
    print(sp)
    print('Initial predictions:')
    print(f'-1  1 : {sp.predict(np.array([1, -1,  1]))}')
    print(f' 1 -1 : {sp.predict(np.array([1,  1, -1]))}')
    print(f'-1 -1 : {sp.predict(np.array([1, -1, -1]))}')
    print(f' 1  1 : {sp.predict(np.array([1,  1,  1]))}')

    times = 1000
    while times:
        sp.train_list(train_list, expected_list)
        times -= 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final predictions:')
    print('Perceptron:')
    print(sp)
    print(f'-1  1 : {sp.predict(np.array([1, -1,  1]))}')
    print(f' 1 -1 : {sp.predict(np.array([1,  1, -1]))}')
    print(f'-1 -1 : {sp.predict(np.array([1, -1, -1]))}')
    print(f' 1  1 : {sp.predict(np.array([1,  1,  1]))}')