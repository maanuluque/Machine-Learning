import pandas as pd
import numpy as np
from types import SimpleNamespace as Obj
from ex1.kohonen import Kohonen

def ex1_a(config):
    csv = pd.read_csv('./ex1/europe.csv', sep=",")
    labels = list(csv.columns)[1:]
    countries = csv.values[:,0]
    data = csv.values[:,1:]

    kohonen = Kohonen(config.k, config.init_radius, config.init_lrate, 
                        config.input_len, config.w_init_mode, data)

    for itr in range(0, 100):
        rand_idx = np.random.randint(config.input_amount)
        kohonen.train(data[rand_idx])