from perceptron.simpleperceptron import SimplePerceptron

def ex1_b():
    w = [0, 0]
    train_list = [
        [-1, 1],
        [1, -1],
        [-1, -1],
        [1, 1]
    ]
    expected_list = [
        1,
        1,
        -1,
        -1,
    ]

    print('LOGICAL XOR:')
    sp = SimplePerceptron(w, 0, 0.1)
    print('Initial Perceptron:')
    print(sp)
    print('Initial predictions:')
    print(f'-1  1 : {sp.predict([-1, 1])}')
    print(f' 1 -1 : {sp.predict([1, -1])}')
    print(f'-1 -1 : {sp.predict([-1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1])}')

    times = 100
    while times:
        sp.train_list(train_list, expected_list)
        times -= 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Final predictions:')
    print('Perceptron:')
    print(sp)
    print(f'-1  1 : {sp.predict([-1, 1])}')
    print(f' 1 -1 : {sp.predict([1, -1])}')
    print(f'-1 -1 : {sp.predict([-1, -1])}')
    print(f' 1  1 : {sp.predict([1, 1])}')