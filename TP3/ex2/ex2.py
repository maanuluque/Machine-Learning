import numpy as np
from numpy import ndarray
from perceptron.multiperceptron import MultiPerceptron
import random
from math import copysign

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

def ex2(data_rows: int, data_cols: int, training_amount: int):
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

    expected_list: list = list(expected_list / expected_list.max())
    expected_list = list(map(lambda exp: [exp], expected_list ))
    training_list = list()
    training_expected_list = list()
    testing_list = list()
    testing_expected_list = list()

    for remaining in range(training_amount, 0, -1):
        idx = random.randint(0, remaining - 1)
        training_list.append(data_list.pop(idx))
        training_expected_list.append(expected_list.pop(idx))

    training_list = np.array(training_list)
    training_expected_list = np.array(training_expected_list)
    testing_list = np.array(data_list)
    testing_expected_list = np.array(expected_list)

    mp = MultiPerceptron(linear_function, linear_derivative, learning_rate=0.2, beta=1, layers=1, layer_dims=[1], data_dim=4)

    times = 1
    while times > 0:
        idx = random.randint(0, training_amount-1)
        mp.train(training_list[idx], training_expected_list[idx])
        times -= 1

    training_predicted_list: ndarray = mp.predict_list(training_list)
    training_errors: ndarray = np.array(np.abs(training_expected_list - training_predicted_list))
    training_errors: ndarray = (1 / 2) * (training_errors ** 2)
    training_err = training_errors.mean()

    testing_predicted_list: ndarray = mp.predict_list(testing_list)
    testing_errors: ndarray = np.array(np.abs(testing_expected_list - testing_predicted_list))
    testing_errors: ndarray = (1 / 2) * (testing_errors ** 2)
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
        for data_size in range(0, data_max + 1, data_step):
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
        err['training_err'] = sum(err['training_err']) / len(err['training_err'])
        err['testing_err'] = sum(err['testing_err']) / len(err['testing_err'])

    for err in error_average_list:
        print(f'Data size: {err["data"]}')
        print(f'Training size: {err["training"]}')
        print(f'Training average error: {err["training_err"]}')
        print(f'Testing  average error: {err["testing_err"]}')


def cross_validation(k, epochs):
    # Retrieve data
    data_max = 200
    data_cols = 3

    group_size = data_max // k

    data_list = list()
    expected_list: ndarray = np.zeros(data_max)
    bias: float = 1
    with open('ex2/ex2-training-set.txt') as f:
        for r, line in enumerate(f):
            if r == data_max:
                break
            data = line.split()
            data_list.append([bias])
            for c in range(0, data_cols):
                data_list[r].append(float(data[c]))
    with open('ex2/ex2-expected-output.txt') as f:
        for r, line in enumerate(f):
            if r == data_max:
                break
            data = line.split()
            expected_list[r] = float(data[0])

    expected_list = list(expected_list / expected_list.max())

    # Divide data randomly in k groups
    k_data_groups = [[] for _ in range(k)]  # list of k lists of data
    k_expected_groups = [[] for _ in range(k)]  # list of k lists of results

    data_remaining = 200 - 1  # starts at 0
    for i in range(k):  # i iterates the k groups
        for j in range(group_size, 0, -1):
            # j iterates inside the i group adding #group_size elements to the corresponding list
            idx = random.randint(0, data_remaining)
            data_remaining -= 1
            k_data_groups[i].append(data_list.pop(idx))
            k_expected_groups[i].append(expected_list.pop(idx))

    k_error_list = [None for _ in range(k)]
    min_group_error = np.inf
    lowest_error_found = {'Group': -1, 'Epoch': -1}
    for i in range(k):
        mp = MultiPerceptron(linear_function, linear_derivative, learning_rate=0.0001, beta=1, layers=1, layer_dims=[1], data_dim=4)
        training_list = list()
        training_expected_list = list()
        for j in range(k):
            if not j == i:  # i is test set, rest are training
                training_list.extend(k_data_groups[j])
                training_expected_list.extend(k_expected_groups[j])

        epoch = 0
        min_epoch_error = np.inf
        min_epoch_error_index = -1
        k_error_list[i] = {
                'training_err': [],
                'testing_err': [],
                'group': i,
                'epoch': []}
        while epoch < epochs:
            # Train Perceptron
            training_list = np.array(training_list)
            training_expected_list = np.array(training_expected_list)
            mp.train_list(training_list, training_expected_list)

            # Evaluate
            training_predicted_list: ndarray = mp.predict_list(training_list)
            training_errors: ndarray = np.array(np.abs(training_expected_list - training_predicted_list))
            training_errors: ndarray = (1 / 2) * (training_errors ** 2)
            training_err = training_errors.mean()

            testing_predicted_list: ndarray = mp.predict_list(np.array(k_data_groups[i]))
            testing_errors: ndarray = np.array(np.abs(np.array(k_expected_groups[i]) - testing_predicted_list))
            testing_errors: ndarray = (1 / 2) * (testing_errors ** 2)
            testing_err = testing_errors.mean()

            min_epoch_error = min(testing_err, min_epoch_error)
            if min_epoch_error == testing_err: min_epoch_error_index = epoch
            epoch += 1

            # results
            k_error_list[i]['training_err'].append(training_err)
            k_error_list[i]['testing_err'].append(testing_err)
            k_error_list[i]['epoch'].append(epoch)

        min_group_error = min(min_epoch_error, min_group_error)
        print("Group #", i + 1, " Epoch #", min_epoch_error_index + 1, " --> error =", min_epoch_error)
        if min_epoch_error == min_group_error:
            lowest_error_found['Group'] = i + 1
            lowest_error_found['Epoch'] = min_epoch_error_index + 1
    return lowest_error_found, k_error_list
