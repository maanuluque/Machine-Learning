import numpy as np
from matplotlib import pyplot as plt
from numpy import ndarray
from ex1.ex1_a import ex1_a
from ex1.ex1_b import ex1_b
from ex2.ex2 import ex2, ex2_stats, cross_validation
from ex3.ex3_a import ex3_a

print('\nEXERCISE 1 A:\n')
ex1_a()
print()

print('\nEXERCISE 1 B:\n')
ex1_b()
 
print('\nEXERCISE 2:\n')
ex2(data_rows=200, data_cols=3, training_amount=150)
print('\n~~ Stats:\n')
ex2_stats()
print('\n~~ Cross validation:\n')
lowest_error, err_list = cross_validation(4, 500)
group = lowest_error['Group']
epoch = lowest_error['Epoch']
print(f'Lowest error found in: Group: {group}, Epoch: {epoch}')

for elem in err_list:
    group = elem['group']
    training_err = err_list[1]['training_err']
    testing_err = err_list[1]['testing_err']
    epochs = err_list[1]['epoch']

    fig, ax = plt.subplots()
    ax.set_ylim([0, 0.5])  # TODO: adjust

    plt.plot(epochs, training_err, label="Training")
    plt.plot(epochs, testing_err, label="Testing")
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.title('Group %i' % group)
    plt.legend()
    plt.show()

print('\nEXERCISE 3 A:\n')
ex3_a()