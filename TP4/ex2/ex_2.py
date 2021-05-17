import pandas as pd
import numpy as np
from ex2.patterns import *
import matplotlib.pyplot as plt
import random


def create_W_single_pattern(pattern):
    if len(pattern.shape) != 1:
        print("The input is not vector")
        return
    else:
        w = np.zeros([len(pattern), len(pattern)])
        for i in range(len(pattern)):
            for j in range(i, len(pattern)):
                if i == j:
                    w[i, j] = 0
                else:
                    w[i, j] = pattern[i] * pattern[j]
                    w[j, i] = w[i, j]
    return w


def energy(weight, x, bias=0):
    # weight: m*m weight matrix
    # x: 1*m data vector
    # bias: outer field
    energy = -x.dot(weight).dot(x.T) + sum(bias * x)
    # E is a scalar
    return energy


def update_asynch(weight, vector, theta=0.5, times=1000000):
    energy_ = []
    times_ = []
    energy_.append(energy(weight, vector))
    times_.append(0)
    for i in range(times):
        length = len(vector)
        # DANGER ZONE
        update_num = random.randint(0, length - 1)
        next_time_value = np.dot(weight[update_num][:], vector) - theta
        # next_time_value = np.dot(weight,vector)  - theta
        # END DANGER ZONE
        if next_time_value >= 0:
            vector[update_num] = 1
        if next_time_value < 0:
            vector[update_num] = -1
        times_.append(i)
        energy_.append(energy(weight, vector))
        # print_pattern()
    return (vector, times_, energy_)


def ex2_a():
    # Get patterns stored and its info
    patterns = letters_pattern()
    patterns_quantity = len(patterns)
    if patterns_quantity != 0:
        fils, cols = patterns[0].shape
    else:
        print("No patterns detected")
        exit()

    # Training stage (set W matrix)
    counter = 0
    for pattern in patterns:
        vector = mat2vector(pattern)
        if counter == 0:
            w_ = create_W_single_pattern(vector)
        else:
            w_ = w_ + create_W_single_pattern(vector)
        counter += 1

    w_ = w_ / (len(vector))
    print("Weight matrix is prepared")
    print()

    # Testing stage
    test_patterns = test_letters_pattern()
    for test_pattern in test_patterns:
        vector = mat2vector(test_pattern)
        print("Pattern to test:")
        print()
        print_pattern(test_pattern)

        original_shape = test_pattern.shape
        data = update_asynch(weight=w_, vector=vector, theta=0.0, times=1000000)
        updated_vector = data[0]
        vector2matrix = updated_vector.reshape(original_shape)
        print("RESULT: ")
        print()
        print_pattern(vector2matrix)
