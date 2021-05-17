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
        # print(f'R: {kohonen.radius} | N: {kohonen.lrate}')
        rand_idx = np.random.randint(config.input_amount)
        kohonen.train(data[rand_idx])
    print(f'R: {kohonen.radius} | N: {kohonen.lrate}')

    X = []
    Y = []
    groups = {}
    
    for idx, country in enumerate(countries):
        w, group = kohonen.predict(data[idx])
        X.append(group[0])
        Y.append(group[1])
        if group not in groups:
            groups[group] = []
        groups[group].append(country)

    for group in groups:
        print(f'Group: {group}:')
        print(groups[group])

    X = np.array(X)
    Y = np.array(Y)

    i = 0
    for group in groups:
        plt.annotate("".join(groups[group]), (X[i], Y[i]))
        i += 1

    plt.scatter(X,Y)
    plt.show()