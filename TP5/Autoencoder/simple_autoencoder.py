from typing import List

import numpy as np
from scipy.optimize import minimize

from multiperceptron import MultiPerceptron
from FileUtils import fonts as fts, functions
from random import randint
import matplotlib.pyplot as plt


def ex_1a():
    # Load classes and set variables
    fonts = fts.Font()
    training_iterations = 100000
    # Choose dataset
    chosen_font = fonts.font2
    # Convert to legible font
    dataset = fts.import_font(chosen_font)
    letter_dimension = dataset[0].size
    rows, cols = dataset.shape

    # Create autoencoder
    mp = MultiPerceptron(functions.sigmoid_function, functions.sigmoid_derivative, learning_rate=0.3, beta=1, layers=5,
                         layer_dims=[letter_dimension, 10, 2, 10, letter_dimension], data_dim=letter_dimension)

    # Set limit for training/testing
    predictions_limit = 10
    # predictions_limit = rows-1

    # Training stage
    for _ in range(0, training_iterations):
        idx = randint(0, predictions_limit)
        mp.train(dataset[idx], dataset[idx])

    # predictions_limit = dataset.shape[0]
    latent_output_x = []
    latent_output_y = []
    for i in range(predictions_limit):
        mp.predict(dataset[i])
        latent_output_x.append(mp.return_latent().activations[0])
        latent_output_y.append(mp.return_latent().activations[1])

    print(latent_output_x)
    print()
    print(latent_output_y)
    # Labels (characters for plot)
    character = 0x40
    labels = []
    number_of_characters = predictions_limit
    for i in range(number_of_characters):
        # print(chr(character))
        character = character + 1
        labels.append(chr(character))

    # Graphs
    plt.style.use('seaborn')
    plt.scatter(latent_output_x, latent_output_y)
    # fig, ax = plt.subplots()
    # ax.scatter(latent_output_x, latent_output_y)
    for i in range(len(latent_output_x)):
        plt.annotate(labels[i], (latent_output_x[i], latent_output_y[i]+0.05))
    plt.xlim(-0.01, 1.1)
    plt.ylim(-0.01, 1.1)
    plt.show()

    # Autoencoder functionality testing
    print(dataset[1].reshape(7, 5))
    print()
    mp.predict(dataset[1])
    print(mp.layers[-1].activations.reshape(7, 5))
    print()
    mp.predict(dataset[2])
    print(dataset[2].reshape(7, 5))
    print(mp.layers[-1].activations.reshape(7, 5))

    # res = opt_sigmoid_function(np.array([2]))
    # #res = minimize(sigmoid_scalar_function, 3)
    # print(res)

# def sigmoid_scalar_function(x):
#     return 1 / (1 + np.math.exp(-2 * x))
#
# def opt_sigmoid_function(x):
#     for i in range(x.shape[0]):
#         res = minimize(sigmoid_scalar_function, x[i])
#         x[i] = res.x
#     return x
#
# def opt2_sigmoid(x):
#     return minimize(sigmoid_scalar_function, x, method='powell')

