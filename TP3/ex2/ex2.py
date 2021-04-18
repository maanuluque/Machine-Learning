import numpy as np
from numpy import ndarray
from perceptron.simpleperceptron import SimplePerceptron

def ex2(training_rows: int, training_cols: int):
    weights: ndarray = np.zeros(training_cols+1)
    training_list: ndarray = np.zeros((training_rows, training_cols+1))
    expected_list: ndarray = np.zeros(training_rows)
    bias: float = 1
    with open('ex2/ex2-training-set.txt') as f:
        for r, line in enumerate(f):
            if r == training_rows:
                break
            data = line.split()
            training_list[r][0] = bias
            for c in range(0, training_cols):
                training_list[r][c+1] = float(data[c])
    with open('ex2/ex2-expected-output.txt') as f:
        for r, line in enumerate(f):
            if r == training_rows:
                break
            data = line.split()
            expected_list[r] = float(data[0])
    
    print(expected_list)
    expected_list = expected_list / expected_list.max()
    print(expected_list)
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    sp = SimplePerceptron(weights, 0.01, 1,  "linear")

    times = 100
    while times > 0:
        sp.train_list(training_list, expected_list)
        times -= 1

    # print(training_list)
    # print(expected_list)

    predicted_list = sp.predict_list(training_list)
    errors: ndarray = np.array(np.abs(expected_list - predicted_list))
    print(errors)
    print(errors.mean())
    print(errors.sum()/errors.size)
    # for idx, predicted in enumerate(predicted_list):
        # print(idx)
        # print(predicted)
        # print(f'ERROR: {predicted - expected_list[idx]}')
    # print(f'{sp.weights}')
    # print(f'{training_list}')