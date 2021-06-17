import numpy as np
from keras.datasets import mnist
from scipy.stats import norm
from VariationalAutoencoder.vae import Vae
import matplotlib.pyplot as plt
from FileUtils.images import generate_photo_matrix

def ej2():
    photo_matrix, people_groups, people_dict = generate_photo_matrix('images', 64, 64, 40, 10)
    photo_matrix = np.array(photo_matrix)
    middle = int(len(photo_matrix)/2)
    x_train = photo_matrix[:middle]
    x_test = photo_matrix[middle:]
    x_train = np.array(x_train).astype('float32') / 255.
    x_test = np.array(x_test).astype('float32') / 255.
    print(len(x_train))
    print(len(x_test))

    input_dim = 64*64
    intermediate_dim = 256
    latent_dim = 2
    batch_size = 100
    epochs = 100

    vae = Vae(input_dim, intermediate_dim, latent_dim)
    vae.fit(x_train, x_train, epochs, batch_size)


    #### ENCODE TEST
    x_test_encoded = vae.encode(x_test, batch_size=batch_size)[0]
    plt.figure(figsize=(6, 6))
    plt.scatter(x_test_encoded[:,0], x_test_encoded[:,1])
    plt.colorbar()
    plt.show()    
    ####################

    #### SHOW GENERATION
    n = 10  # figure with 10x10 faces
    face_size = 64
    figure = np.zeros((face_size * n, face_size * n))
    grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
    grid_y = norm.ppf(np.linspace(0.05, 0.95, n))
    for i, yi in enumerate(grid_x):
        for j, xi in enumerate(grid_y):
            z_sample = np.array([[xi, yi]])
            x_decoded = vae.decode(z_sample)
            face = x_decoded[0].reshape(face_size, face_size)
            figure[i * face_size: (i + 1) * face_size,
                j * face_size: (j + 1) * face_size] = face
    plt.figure(figsize=(10, 10))
    plt.imshow(figure, cmap='Greys_r')
    plt.show()
    ####################
