from perceptron.simpleperceptron import SimplePerceptron

def ex1_a():
    w = [0, 0]
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
    sp = SimplePerceptron(w, 0, 0.5)
    print('Initial Perceptron:')
    print(sp)
    print('Initial predictions:')
    print(f'-1  1 : {sp.predict([-1, 1])}')
    print(f' 1 -1 : {sp.predict([1, -1])}')
    print(f'-1 -1 : {sp.predict([-1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1])}')
    sp.train_list(train_list, expected_list)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final Perceptron:')
    print(sp)
    print('Final predictions:')
    print(f'-1  1 : {sp.predict([-1, 1])}')
    print(f' 1 -1 : {sp.predict([1, -1])}')
    print(f'-1 -1 : {sp.predict([-1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1])}')