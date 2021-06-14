import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.layers import Input, Dense, Lambda, Reshape
from keras.models import Model
from keras import backend as K
from keras import metrics
from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()

class Vae:
    def __init__(self, input_dim, intermediate_dim, latent_dim):
        self.input_dim = input_dim
        self.intermediate_dim = intermediate_dim
        self.latent_dim = latent_dim
        self.epsilon_mean = 0.
        self.epsilon_stddev = 1.0
        self.sample_z = self.generate_sample_z()
        self.encoder = self.generate_encoder()
        self.decoder = self.generate_decoder()
        self.lower_bound = self.generate_lower_bound()
        self.autoencoder = self.generate_autoencoder()

    def generate_sample_z(self):
        def fun(args: tuple):
            x_mean, x_variance = args
            epsilon = K.random_normal(shape=(K.shape(x_mean)[0], self.latent_dim), mean=self.epsilon_mean, stddev=self.epsilon_stddev)
            return x_mean + K.exp(x_variance / 2) * epsilon 
        return fun

    def generate_encoder(self):
        self.x_input = Input(shape=(self.input_dim,), name="input")
        h = Dense(self.intermediate_dim, activation='relu', name="encoding")(self.x_input)
        self.x_mean = Dense(self.latent_dim, name="mean")(h)
        self.x_variance = Dense(self.latent_dim, name="log-variance")(h)
        z = Lambda(self.sample_z, output_shape=(self.latent_dim,))([self.x_mean, self.x_variance])
        return Model(self.x_input, [self.x_mean, self.x_variance, z], name="encoder")

    def generate_decoder(self):
        input_decoder = Input(shape=(self.latent_dim,), name="decoder_input")
        decoder_h = Dense(self.intermediate_dim, activation='relu', name="decoder_h")(input_decoder)
        x_decoded = Dense(self.input_dim, activation='sigmoid', name="flat_decoded")(decoder_h)
        return Model(input_decoder, x_decoded, name="decoder")

    def generate_lower_bound(self):
        def fun(x: tf.Tensor, x_decoded_mean: tf.Tensor):
            xent_loss = self.input_dim * metrics.binary_crossentropy(x, x_decoded_mean) # x-^X
            kl_loss = - 0.5 * K.sum(1 + self.x_variance - K.square(self.x_mean) - K.exp(self.x_variance), axis=-1)
            return K.mean(xent_loss + kl_loss)
        return fun

    def generate_autoencoder(self):
        output_combined = self.decoder(self.encoder(self.x_input)[self.latent_dim])
        vae = Model(self.x_input, output_combined)
        vae.compile(loss=self.lower_bound,experimental_run_tf_function=False)
        return vae
    
    def fit(self, x_train, y_train, epochs, batch_size):
        self.autoencoder.fit(x_train, y_train, shuffle=True, epochs=epochs, batch_size=batch_size)

    def encode(self, x, batch_size):
        return self.encoder.predict(x, batch_size=batch_size)

    def decode(self, z):
        return self.decoder.predict(z)