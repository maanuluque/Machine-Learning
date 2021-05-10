import numpy as np
from numpy import ndarray as arr
from math import floor, ceil

class Kohonen:
    def __init__(self, k, radius, lrate, input_len, w_init_mode, inputs:arr=None):
        self.k = k
        self.radius = radius
        self.lrate = lrate
        self.net = self.generate_net(k, input_len, w_init_mode, inputs)
        self.update_radius = lambda x: x
        self.update_lrate = lambda x: 1/x

    def generate_net(self, k, input_len, w_init_mode, inputs:arr=None):
        if w_init_mode == "random":
            return np.random.rand(k, k, input_len)
        elif w_init_mode == "input":
            net = np.zeros((k, k, input_len))
            for row in net:
                for neuron_weights in row:
                    input_amount = inputs.shape[0]
                    rand_idx = np.random.randint(input_amount)
                    for idx, value in enumerate(inputs[rand_idx]):
                        neuron_weights[idx] = value
            return net
        else:
            raise Exception('Invalid weights initialization mode.')

    def train(self, inputs:arr):
        std_inputs = ( inputs - inputs.mean()) / inputs.std()
        closest_neuron, closest_neuron_idx = self.find_closest_neuron(std_inputs)
        neuron_nhbs = self.find_neuron_neighbours(closest_neuron_idx)
        self.update_weights(neuron_nhbs, closest_neuron, inputs)
        self.radius = self.update_radius(self.radius)
        self.lrate = self.update_lrate(self.lrate)
        
    def find_closest_neuron(self, inputs):
        closest_neuron: arr = None
        closest_distance = float('inf') 
        closest_idx: tuple = None
        row_i = 0
        for row in self.net:
            col_i = 0
            for neuron_weights in row:
                dist = np.linalg.norm(neuron_weights - inputs)
                if dist < closest_distance:
                    closest_neuron = neuron_weights
                    closest_distance = dist
                    closest_idx = (row_i, col_i)
                col_i += 1
            row_i += 1

        return closest_neuron, closest_idx

    def find_neuron_neighbours(self, idx):
        neighbours = list()
        row_min = max([0, floor(idx[0] - self.radius)])
        row_max = min([self.k, ceil(idx[0] + self.radius)])
        col_min = max([0, floor(idx[1] - self.radius)])
        col_max = min([self.k, ceil(idx[1] + self.radius)])
        for row in range(row_min, row_max):
            for col in range(col_min, col_max):
                if ((row, col) != idx):
                    nhb = np.array([row, col])
                    p = np.array(idx)
                    if np.linalg.norm(nhb - p) <= self.radius:
                        neighbours.append(self.net[row][col])
        return neighbours

    def update_weights(self, weight_list, matched_weights, inputs):
        for weights in weight_list:
            for idx, w in enumerate(weights):
                weights[idx] = w + self.lrate * (inputs[idx] - matched_weights[idx])


    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl} k: {self.k}{nl} rate: {self.lrate}{nl} radius: {self.radius}{nl} net: {self.net}{nl}{cl}'