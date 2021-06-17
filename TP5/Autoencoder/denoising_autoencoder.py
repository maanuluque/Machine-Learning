import numpy
from sklearn.preprocessing import minmax_scale

from FileUtils.fonts import count_accepted
from multiperceptron import MultiPerceptron
from FileUtils import fonts as fts, functions
from random import randint
import matplotlib.pyplot as plt


def ex_1b(noise_method, noise_magnitude, noise_probability, mean, sigma):
    print("EXERCISE 1.B:")
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

    predictions_limit = 5
    data = []
    noise = []
    for i in range(1, predictions_limit + 1):
        data.append(dataset[i])
        noise.append(add_noise(noise_method, noise_magnitude, noise_probability, mean, sigma, dataset[i]))
    noise = numpy.array(noise)
    data = numpy.array(data)


    # Create autoencoder
    mp = MultiPerceptron.new_optimized(tanh_function, tanh_derivative, learning_rate=0.001, beta=1, layers=11,
                                       layer_dims=[letter_dimension, 25, 17, 10, 5, 2, 5, 10, 17, 25, letter_dimension],
                                       data_dim=letter_dimension, inputs=noise, expected=data)

    # prediction
    accepted_values = 0
    for i in range(predictions_limit):
        print("No noise:")
        print(data[i].reshape(7, 5))
        print()
        print("With noise:")
        print(noise[i].reshape(7, 5))
        print("------------")
        mp.predict(noise[i])
        output = mp.layers[-1].activations
        print("Output:")
        print(output.reshape(7, 5))
        print()
        accepted = fts.count_accepted(0.1, data[i], output)
        print(accepted)
        if accepted: accepted_values += 1
        print()
    print(f'Accepted: {accepted_values}')


def add_noise(noise_method, noise_magnitude, noise_probability, mean, sigma, x):
    noisy = []

    if noise_method == 's&p':
        for i in range(len(x)):
            prob = numpy.random.uniform(0, 1)
            if prob >= noise_probability:
                if x[i] == 1:
                    noisy.append(-1)
                else:
                    noisy.append(1)
            else:
                noisy.append(x[i])
    elif noise_method == 'gauss':
        for i in range(len(x)):
            gaussian = numpy.random.normal(mean, sigma, x.shape)
            noisy.append(x[i] + gaussian[i])
        noisy = minmax_scale(noisy, feature_range=(-1, 1))
    else:
        for i in range(len(x)):
            delta = numpy.random.uniform(0, noise_magnitude)
            if x[i] == 1:
                noisy.append(x[i] - delta)
            else:
                noisy.append(x[i] + delta)
    return noisy


def tanh_function(x):
    return numpy.tanh(x)


# Assuming y = tanh(x)
def tanh_derivative(y):
    return 1 - (y ** 2)
