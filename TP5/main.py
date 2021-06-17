from Autoencoder import simple_autoencoder, denoising_autoencoder
from VariationalAutoencoder.ej2 import ej2

def main():
    #simple_autoencoder.ex_1a()
    # method can be [ uniform, s&p, gauss]
    # magnitude is for uniform, probability for salt and pepper, mean and sigma for gauss
    denoising_autoencoder.ex_1b(noise_method='s&p', noise_magnitude=0.1, noise_probability=0.6, mean=0.5, sigma=0.2)
    # ej2()

if __name__ == "__main__":
    main()
