import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from types import SimpleNamespace as Obj
from ex1.kohonen import Kohonen

def ex1_a(config):
    csv = pd.read_csv('./ex1/europe.csv', sep=",")
    labels = list(csv.columns)[1:]
    countries = csv.values[:,0]
    data = csv.values[:,1:]

    kohonen = Kohonen(config.k, config.init_radius, config.radius_modifier, config.init_lrate,
                    config.lrate_modifier, config.input_len, config.w_init_mode, data)

    print(f'R: {kohonen.radius} | N: {kohonen.lrate}')
    for itr in range(0, 500*len(data)):
        rand_idx = np.random.randint(config.input_amount)
        kohonen.train(data[rand_idx])
    print(f'R: {kohonen.radius} | N: {kohonen.lrate}')

    groups = {}
    points = []
    for idx, country in enumerate(countries):
        w, group = kohonen.predict(data[idx])
        if group not in groups:
            groups[group] = Obj()
            groups[group].countries = []
            groups[group].point = (group[0], group[1])
        groups[group].countries.append(country)


    X = []
    Y = []
    labels = []
    count = []
    i = 0
    for group in groups:
        strings = "\n".join(groups[group].countries)
        x = groups[group].point[0]
        y = groups[group].point[1]
        X.append(x)
        Y.append(y)
        labels.append(strings)
        c = len(groups[group].countries)
        count.append(c)
        print(f'Group ({x},{y}): {c} countries')
        print(strings)
        strings = strings + "\n" + str(c)
        plt.annotate(strings, groups[group].point)
        i += 1
    plt.scatter(X, Y)
    im = np.zeros((config.k, config.k))
    for x, y, c in zip(X, Y, count):
        im[x, y] = c

    plt.imshow(im.T, cmap=plt.cm.get_cmap('summer', 28))
    plt.colorbar()
    plt.title("Country groups")
    plt.show()

    # U-MATRIX ~~ DANGER ZONE ~~
    u_matrix = kohonen.get_u_matrix()
    print('U Matrix:')
    print(u_matrix)
    plt.title("U matrix")
    plt.imshow(u_matrix, cmap='gray')
    plt.colorbar()

    plt.show()
