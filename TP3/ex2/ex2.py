import numpy as np
from numpy import ndarray
from perceptron.simpleperceptron import SimplePerceptron
import random

def ex2(data_rows: int, data_cols: int, training_amount: int):
    weights: ndarray = np.zeros(data_cols+1)
    data_list = list()
    expected_list: ndarray = np.zeros(data_rows)
    bias: float = 1
    with open('ex2/ex2-training-set.txt') as f:
        for r, line in enumerate(f):
            if r == data_rows:
                break
            data = line.split()
            data_list.append([bias])
            for c in range(0, data_cols):
                data_list[r].append(float(data[c]))
    with open('ex2/ex2-expected-output.txt') as f:
        for r, line in enumerate(f):
            if r == data_rows:
                break
            data = line.split()
            expected_list[r] = float(data[0])

    expected_list = list(expected_list / expected_list.max())
    training_list = list()
    training_expected_list = list()
    testing_list = list()
    testing_expected_list = list()

    for remaining in range(training_amount, 0, -1):
        idx = random.randint(0, remaining-1)
        training_list.append(data_list.pop(idx))
        training_expected_list.append(expected_list.pop(idx))

    training_list = np.array(training_list)
    training_expected_list = np.array(training_expected_list)
    testing_list = np.array(data_list)
    testing_expected_list = np.array(expected_list)

    sp = SimplePerceptron(weights, 0.0001, 1,  "linear")

    times = 10000
    while times > 0:
        sp.train_list(training_list, training_expected_list)
        times -= 1

    training_predicted_list: ndarray = sp.predict_list(training_list)
    training_errors: ndarray = np.array(np.abs(training_expected_list - training_predicted_list))
    training_errors: ndarray = (1/2)*(training_errors**2)
    training_err = training_errors.mean()

    testing_predicted_list: ndarray = sp.predict_list(testing_list)
    testing_errors: ndarray = np.array(np.abs(testing_expected_list - testing_predicted_list))
    testing_errors: ndarray = (1/2)*(testing_errors**2)
    testing_err = testing_errors.mean()

    return training_err, testing_err

def ex2_stats():
    data_max = 200
    data_step = 50
    train_step = 25
    error_list = list()
    total_times = 0
    iterations = 2
    for i in range(0, iterations):
        print()
        print(f'ITERATION {i}')
        iter_errors_list = list()
        for data_size in range(0, data_max+1, data_step):
            for training_size in range(train_step, data_size, train_step):
                print(f'({i})> Running data: {data_size}, training: {training_size}...')
                total_times += 1
                training_err, testing_err = ex2(data_size, 3, training_size)
                iter_errors_list.append({
                    'training_err': training_err, 
                    'testing_err': testing_err, 
                    'data': data_size,
                    'training': training_size})
        error_list.append(iter_errors_list)
    
    error_average_list = list()
    for _ in range(0, len(error_list[0])):
        error_average_list.append({'training_err': [], 'testing_err': [], 'data': 0, 'training': 0})
    
    for _, err_list in enumerate(error_list):
        for idx, err in enumerate(err_list):
            error_average_list[idx]['data'] = err['data']
            error_average_list[idx]['training'] = err['training']
            error_average_list[idx]['training_err'].append(err['training_err'])
            error_average_list[idx]['testing_err'].append(err['testing_err'])
    
    for idx, err in enumerate(error_average_list):
        err['training_err'] = sum(err['training_err'])/len(err['training_err'])
        err['testing_err'] = sum(err['testing_err'])/len(err['testing_err'])
    
    for err in error_average_list:
        print(f'Data size: {err["data"]}')
        print(f'Training size: {err["training"]}')
        print(f'Training average error: {err["training_err"]}')
        print(f'Testing  average error: {err["testing_err"]}')