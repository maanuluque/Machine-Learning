from typing import List
import numpy as np
from scipy.optimize import minimize

from multiperceptron import MultiPerceptron
from FileUtils import fonts as fts, functions
from random import randint
import matplotlib.pyplot as plt

def tanh_function(x):
    return np.tanh(x)

# Assuming y = tanh(x)
def tanh_derivative(y):
    return 1 - (y ** 2)

def ex_1a():
    # Load classes and set variables
    fonts = fts.Font()
    training_iterations = 1000
    # Choose dataset
    chosen_font = fonts.font2
    # Convert to legible font
    dataset = fts.import_font(chosen_font)
    letter_dimension = dataset[0].size
    rows, cols = dataset.shape

    # Pre-processing
    dataset = fts.pre_tanh(dataset)

    predictions_limit = 2
    data = []
    for i in range(predictions_limit):
        data.append(dataset[i])

    # mp = MultiPerceptron.new(tanh_function, tanh_derivative, learning_rate=0.001,
    #                      beta=1, layers=11, layer_dims=[letter_dimension, 35, 25, 17, 10, 5, 2, 5, 10, 17, 25, 35, letter_dimension],
    #                      data_dim=letter_dimension)

    # # Set limit for training/testing
    # for _ in range(training_iterations):
    #     # idx = randint(0, 1, 4-1)
    #     # mp.train(data[idx], data[idx])
    #     for i in range(3):
    #         mp.train(data[i], data[i])
    data = np.array(data)
    mp = MultiPerceptron.new_optimized(tanh_function, tanh_derivative, learning_rate=0.001,
                         beta=1, layers=11, layer_dims=[letter_dimension, 25, 17, 10, 5, 2, 5, 10, 17, 25, letter_dimension],
                         data_dim=letter_dimension, inputs=data, expected=data)

    latent_output_x = []
    latent_output_y = []

    # Autoencoder testing and 2D Graph
    min_error = 0.5
    accepted_values = 0
    for i in range(predictions_limit):
        print(dataset[i].reshape(7, 5))
        print()
        mp.predict(dataset[i])
        output = mp.layers[-1].activations
        # output = fts.cast_delta(0.5, output)
        print(output.reshape(7, 5))
        print()
        accepted = fts.count_accepted(min_error, dataset[i], output)
        print(accepted)
        if accepted: accepted_values += 1
        print()

        # For graphs
        latent_output_x.append(mp.return_latent().activations[0])
        latent_output_y.append(mp.return_latent().activations[1])

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
        plt.annotate(labels[i], (latent_output_x[i], latent_output_y[i] + 0.05))
    plt.xlim(-1.01, 1.1)
    plt.ylim(-1.01, 1.1)
    plt.show()
    print("Accepted values are: " + str(accepted_values))

    # Generate a new value

    # point = [0.2, 0.3]
    # print("Generating new value..")
    # print("Input: " + str(point))
    # mp.predict_from_latent(np.array(point))
    # print(mp.layers[-1].activations.reshape(7, 5))

