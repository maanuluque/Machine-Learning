from simpleperceptron import SimplePerceptron

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

sp = SimplePerceptron(w1, 0, 2, 0.5)
print('Initial predictions:')
print('Perceptron:')
print(sp)
print(f'-1  1 : {sp.predict([-1, 1])}')
print(f' 1 -1 : {sp.predict([1, -1])}')
print(f'-1 -1 : {sp.predict([-1, -1])}')
print(f' 1  1 : {sp.predict([1, 1])}')
sp.train_list(train_list, expected_list)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
print('Final predictions:')
print('Perceptron:')
print(sp)
print(f'-1  1 : {sp.predict([-1, 1])}')
print(f' 1 -1 : {sp.predict([1, -1])}')
print(f'-1 -1 : {sp.predict([-1, -1])}')
print(f' 1  1 : {sp.predict([1, 1])}')