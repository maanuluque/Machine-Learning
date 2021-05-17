import numpy as np

def letters_pattern():
    letters = {
        "A": [
            [-1,  1,  1,  1, -1],
            [ 1, -1, -1, -1,  1],
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1]
        ],
        # "B": [
        #     [ 1,  1,  1,  1, -1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1,  1,  1,  1,  1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1,  1,  1,  1, -1]
        # ],
        "C": [
            [-1,  1,  1,  1,  1],
            [ 1, -1, -1, -1, -1],
            [ 1, -1, -1, -1, -1],
            [ 1, -1, -1, -1, -1],
            [-1,  1,  1,  1,  1]
        ],
        # "D": [
        #     [ 1,  1,  1,  1, -1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1,  1,  1,  1, -1]
        # ]
        # ,
        "E": [
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1, -1],
            [ 1,  1,  1,  1, -1],
            [ 1, -1, -1, -1, -1],
            [ 1,  1,  1,  1,  1]
        ]
        ,
        "H": [
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1]
        ]
        ,
        "X": [
            [ 1, -1, -1, -1,  1],
            [-1,  1, -1,  1, -1],
            [-1, -1,  1, -1, -1],
            [-1,  1, -1,  1, -1],
            [ 1, -1, -1, -1,  1]
        ]
    }

    return np_letters_pattern(letters)

def np_letters_pattern(letters_dictionary):
    np_patterns = []
    for key in letters_dictionary.keys():
        letters_array = np.array(
            letters_dictionary[key]
        )
        np_patterns.append(letters_array)
    return np_patterns

def print_pattern(pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if pattern[i][j] == 1:
                print("1", end = '')
            else:
                print(" ", end = '')
        print()
    print()

def mat2vector(pattern):
    m = pattern.shape[0]*pattern.shape[1]
    vector = np.zeros(m)
    
    element = 0
    for i in range(pattern.shape[0]):
        for j in range(pattern.shape[1]):
            vector[element] = pattern[i,j]
            element += 1
    return vector

def test_letters_pattern():
    letters = {
        "A": [
            [-1,  1,  1,  1, -1],
            [ 1, -1, -1, -1,  1],
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1]
         ]
        #  ,
        # "B": [
        #     [ 1,  1,  1,  1, -1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1,  1,  1,  1,  1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1,  1,  1,  1, -1]
        # ]
        ,
        "C": [
            [-1,  1,  1,  1,  1],
            [ 1, -1, -1, -1, -1],
            [ 1, -1, -1, -1, -1],
            [ 1, -1, -1, -1, -1],
            [-1,  1,  1,  1,  1]
        ]
        ,
        # "D": [
        #     [ 1,  1,  1,  1, -1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1, -1, -1, -1,  1],
        #     [ 1,  1,  1,  1, -1]
        # ]
        # ,
        "E": [
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1, -1],
            [ 1,  1,  1,  1, -1],
            [ 1, -1, -1, -1, -1],
            [ 1,  1,  1,  1,  1]
        ]
                ,
        "H": [
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1]
        ]
        ,
        "X": [
            [ 1, -1, -1, -1,  1],
            [-1,  1, -1,  1, -1],
            [-1, -1,  1, -1, -1],
            [-1,  1, -1,  1, -1],
            [ 1, -1, -1, -1,  1]
        ]
        ,
        "A_bad": [
            [-1,  1,  1,  1, -1],
            [ 1, -1, -1, -1,  1],
            [ 1,  1, -1, -1,  1],
            [ 1, -1, -1, -1,  1],
            [ 1, -1, -1, -1,  1]
         ]
         ,
        "E_bad": [
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1, -1],
            [ 1,  1,  1,  1,  1],
            [ 1, -1, -1, -1, -1],
            [ 1,  1,  1,  1, -1]
        ]
        ,
    }

    return np_letters_pattern(letters)