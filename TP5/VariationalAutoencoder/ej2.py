import numpy as np
from keras.datasets import mnist
from scipy.stats import norm
from VariationalAutoencoder.vae import Vae
import matplotlib.pyplot as plt

def ej2():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    input_dim = 28*28
    intermediate_dim = 256
    latent_dim = 2
    batch_size = 100
    epochs = 50

    vae = Vae(input_dim, intermediate_dim, latent_dim)
    vae.fit(x_train, x_train, epochs, batch_size)

    x_test_encoded = vae.encode(x_test, batch_size=batch_size)[0]

    plt.figure(figsize=(6, 6))
    plt.scatter(x_test_encoded[:,0], x_test_encoded[:,1], c=y_test, cmap='viridis')
    plt.colorbar()
    plt.show()

    n = 15  # figure with 15x15 digits
    digit_size = 28
    figure = np.zeros((digit_size * n, digit_size * n))
    grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
    grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

    for i, yi in enumerate(grid_x):
        for j, xi in enumerate(grid_y):
            z_sample = np.array([[xi, yi]])
            x_decoded = vae.decode(z_sample)
            digit = x_decoded[0].reshape(digit_size, digit_size)
            figure[i * digit_size: (i + 1) * digit_size,
                j * digit_size: (j + 1) * digit_size] = digit

    plt.figure(figsize=(10, 10))
    plt.imshow(figure, cmap='Greys_r')
    plt.show()
