import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pca import pca

def ex1_b(config):


    csv = pd.read_csv('./ex1/europe.csv', sep=",")
    labels = list(csv.columns)[1:]
    countries = csv.values[:, 0]
    data = csv.values[:, 1:]
    x = StandardScaler().fit_transform(data)
    w = np.random.normal(size=(7, 1))
    learning_rate = 0.005
    epochs = 100
    i = 0

    while np.linalg.norm(w) != 1:
        y = np.dot(x, w)
        w += learning_rate * np.sum(y * x - np.square(y) * w.T, axis=0).reshape((7, 1))
        i += 1

    print("Our PC1")
    pc1 = (x @ w).reshape((1, 28))
    print(pc1)
    print("Converged in: ", i, " epochs")
    model = pca(n_components=2)
    res = model.fit_transform(x)
    pcaValues = res['PC'].get('PC1').values
    print('PCA')
    print(np.array(pcaValues))

    countriesSort = []
    for idx, r in enumerate(pcaValues):
        countriesSort.append((r, idx))
    countriesSort.sort()
    print('Countries')
    for c in countriesSort:
        print(f'{countries[c[1]]}: {c[0]}')

    fig, ax = model.biplot(n_feat=7, y=np.array(countries))
