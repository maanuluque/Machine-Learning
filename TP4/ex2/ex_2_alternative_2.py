import numpy as np
from ex2.patterns import *

def sgn_function(vector):
    result = np.zeros(shape=len(vector))
    for index in range(len(result)):
        if vector[index] >= 0:
            result[index] = 1
        else:
            result[index] = -1
    return result
    # print(result)
    # print(result.shape)


def iteration_function(w_, pattern, times=100000):
    product = np.matmul(np.transpose(pattern), w_)
    sgn_vector = sgn_function(product)
    for i in range(times):
        product = np.matmul(sgn_vector, w_)
        sgn_vector = sgn_function(product)
    return sgn_vector

def test_mat2vector():
    patterns = letters_pattern()
    patterns_quantity = len(patterns)
    if patterns_quantity != 0:
        fils, cols = patterns[0].shape
    else:
        print("No patterns detected")
        exit()

    print("Pattern is: ")
    original_shape = patterns[0].shape
    print_pattern(patterns[0])
    vector = mat2vector(patterns[0])
    vector2matrix = vector.reshape(original_shape)
    print_pattern(vector2matrix)


def calculate_W(patterns):
    # Recibo una lista de los patrones (lista de matrices)

    patterns_vector = []
    for pattern in patterns:
        pattern_vector = mat2vector(pattern)
        patterns_vector.append(pattern_vector)
    # Hasta aca ya los pase a vectores

    counter = 1
    for pattern_vector in patterns_vector:
        if counter == 1:
            product = np.outer(pattern_vector, np.transpose(pattern_vector))
            identity = np.identity(product.shape[0])
            w_ = product - identity
            counter += 1
        else:
            product = np.outer(pattern_vector, np.transpose(pattern_vector))
            identity = np.identity(product.shape[0])
            temp = product - identity
            w_ += temp

    # Finalmente, fuerzo la diagonal con ceros
    # fils, cols = w_.shape
    # for i in range(fils):
    #     for j in range(cols):
    #         if i == j:
    #             w_[i, j] = 0
    return w_

def ex_2_a_alternative_2():
    patterns = letters_pattern()
    patterns_quantity = len(patterns)
    if patterns_quantity != 0:
        fils, cols = patterns[0].shape
    else:
        print("No patterns detected")
        exit()

    # Cheked: w_ is a matrix with 25x25 with diagonal = 0
    w_ = calculate_W(patterns)

    # Testing stage
    test_patterns = test_letters_pattern()
    for test_pattern in test_patterns:
        original_shape = test_pattern.shape
        vector = mat2vector(test_pattern)
        print("Pattern to test:")
        print()
        print_pattern(test_pattern)
        updated_vector = iteration_function(w_, vector, times=100000)
        # updated_vector = data[0]
        vector2matrix = updated_vector.reshape(original_shape)
        print("RESULT: ")
        print()
        # print(updated_vector)
        print_pattern(vector2matrix)
