import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray
from ex1.ex1_a import ex1_a
from ex1.ex1_b import ex1_b
from ex2.ex2 import ex2, ex2_stats, cross_validation

# print('EXERCISE 1 A:')
# ex1_a()
# print()

# print('EXERCISE 1 B:')
# ex1_b()

print('EXERCISE 2:')
lowest_error, err_list = cross_validation(4, 100)
group = lowest_error['Group']
epoch = lowest_error['Epoch']
print(f'Lowest error found in: Group: {group}, Epoch: {epoch}')

for elem in err_list:
    group = elem['group']
    training_err = err_list[1]['training_err']
    testing_err = err_list[1]['testing_err']
    epochs = err_list[1]['epoch']

    fig, ax = plt.subplots()
    ax.set_ylim([0, 0.05])  # TODO: adjust

    plt.plot(epochs, training_err, label="Training")
    plt.plot(epochs, testing_err, label="Testing")
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Group %i' % group)
    plt.legend()
    plt.show()

