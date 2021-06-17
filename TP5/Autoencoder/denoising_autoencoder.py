import numpy
from sklearn.preprocessing import minmax_scale

from multiperceptron import MultiPerceptron
from FileUtils import fonts as fts, functions
from random import randint
import matplotlib.pyplot as plt


def ex_1b(noise_method, noise_magnitude, noise_probability, mean, sigma):

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
    noisy = add_noise(noise_method, noise_magnitude, noise_probability, mean, sigma, dataset[1])
    print(dataset[1].reshape(7, 5))
    np = numpy.asarray(noisy)
    noisy = np.reshape(7, 5)
    print(noisy)

    return

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


def add_noise(noise_method, noise_magnitude, noise_probability, mean, sigma, x):
    noisy = []
    if noise_method == 'uniform':
        for i in range(len(x)):
            delta = numpy.random.uniform(0, noise_magnitude)
            if x[i] == 1:
                noisy.append(x[i] - delta)
            else:
                noisy.append(x[i] + delta)
    elif noise_method == 's&p':
        for i in range(len(x)):
            prob = numpy.random.uniform(0, 1)
            if prob >= noise_probability:
                if x[i] == 1:
                    noisy.append(0)
                else:
                    noisy.append(1)
            else:
                noisy.append(x[i])
    elif noise_method == 'gauss':
        for i in range(len(x)):
            gaussian = numpy.random.normal(mean, sigma, x.shape)
            noisy.append(x[i] + gaussian[i])
        noisy = minmax_scale(noisy, feature_range=(0, 1))
    return noisy
