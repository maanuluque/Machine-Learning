import functions
from multiperceptron import MultiPerceptron
import fonts as fts
from random import randint


def simple_autoencoder():
    # Load classes and set variables
    fonts = fts.Font()
    training_iterations = 10000
    # Choose dataset
    chosen_font = fonts.font2
    # Convert to legible font
    dataset = fts.import_font(chosen_font)
    letter_dimension = dataset[0].size
    rows, cols = dataset.shape

    mp = MultiPerceptron(functions.tanh_function, functions.tanh_derivative, learning_rate=0.2, beta=1, layers=3,
                         layer_dims=[letter_dimension, 2, letter_dimension], data_dim=letter_dimension)

    for _ in range(0, training_iterations):
        idx = randint(0, rows - 1)
        mp.train(dataset[idx], dataset[idx])

    latent_layer = mp.return_latent()
    # print(latent_layer)

    #print(f' c : {mp.predict(dataset[3])}')
