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
    product = np.dot(w_, pattern)
    sgn_vector = sgn_function(product)
    for i in range(times):
        product = np.dot(w_, product)
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
    # Lo primero que hago es pasarlos a vectores
    # Despues, los voy agregando como columnas
    # k_ va a ser una lista con los patrones en vectores, en columnas.
    patterns_vector = []
    for pattern in patterns:
        pattern_vector = mat2vector(pattern)
        patterns_vector.append(pattern_vector)
    neurons_number = len(patterns_vector[0])
    k_np = np.zeros(shape=(neurons_number, len(patterns_vector)))
    # for pattern_vect in patterns_vector:
    for j in range(k_np.shape[1]):
        for i in range(k_np.shape[0]):
            # Aca puedo poner a diagonal :p
            k_np[i, j] = patterns_vector[j][i]

    identity = np.identity(k_np.shape[0])
    transposed = np.transpose(k_np)
    product = np.dot(k_np, transposed)
    w_ = (1 / neurons_number) * product  # -identity

    # Finalmente, fuerzo la diagonal con ceros
    fils, cols = w_.shape
    for i in range(fils):
        for j in range(cols):
            if i == j:
                w_[i, j] = 0
    return w_

def ex_2_a_alternative():
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
        updated_vector = iteration_function(w_, vector, times=1000)
        # updated_vector = data[0]
        vector2matrix = updated_vector.reshape(original_shape)
        print("RESULT: ")
        print()
        # print(updated_vector)
        print_pattern(vector2matrix)
