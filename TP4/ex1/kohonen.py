import numpy as np
from numpy import ndarray as arr
from math import floor, ceil

class Kohonen:
    def __init__(self, k, radius, radius_modifier, lrate, lrate_modifier, input_len, w_init_mode, inputs:arr=None):
        self.k = k
        self.radius = radius
        self.init_radius = radius
        self.radius_modifier = radius_modifier
        self.lrate = float(lrate)
        self.lrate_modifier = float(lrate_modifier)
        self.net = self.generate_net(k, input_len, w_init_mode, inputs)
        self.iter = 0

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

    def predict(self, inputs: arr):
        aux = ( inputs - inputs.mean()) / inputs.std()
        std_inputs = aux / np.linalg.norm(aux)
        closest_neuron, closest_neuron_idx = self.find_closest_neuron(std_inputs)
        return closest_neuron, closest_neuron_idx

    def train(self, inputs:arr):
        aux = ( inputs - inputs.mean()) / inputs.std()
        std_inputs = aux / np.linalg.norm(aux)
        closest_neuron, closest_neuron_idx = self.find_closest_neuron(std_inputs)
        neuron_nhbs = self.find_neuron_neighbours(closest_neuron_idx)
        self.update_weights(neuron_nhbs, closest_neuron, std_inputs)
        self.iter += 1
        self.radius = 1 + (self.init_radius - 1)*(np.e**(-self.radius_modifier*self.iter))
        self.lrate = 1/((self.iter*self.lrate_modifier)+1)
        
    def find_closest_neuron(self, inputs):
        closest_neuron: arr = None
        closest_distance = float('inf') 
        closest_idx: tuple = None
        row_i = 0
        for row in self.net:
            col_i = 0
            for neuron_weights in row:
                dist = np.linalg.norm(inputs - neuron_weights)
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
        row_max = min([self.k, ceil(idx[0] + self.radius)+1])
        col_min = max([0, floor(idx[1] - self.radius)])
        col_max = min([self.k, ceil(idx[1] + self.radius)+1])
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
                weights[idx] = w + self.lrate * (inputs[idx] - w)

    def get_u_matrix(self):
        net_shape = self.net.shape
        k = net_shape[0]
        u_matrix = np.zeros((k, k))
        for i, row in enumerate(self.net):
            for j, neuron in enumerate(row): 
                nbhd_dist = list()
                for nhb in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nhb_i = i + nhb[0]
                    nhb_j = j + nhb[1]
                    if (nhb_i >= 0 and nhb_i < k and nhb_j >= 0 and nhb_j < k):
                        nbhd_dist.append(np.linalg.norm(neuron - self.net[nhb_i][nhb_j]))
                avg = np.average(np.array(nbhd_dist))
                u_matrix[i][j] = avg  
        return u_matrix


    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl} k: {self.k}{nl} rate: {self.lrate}{nl} radius: {self.radius}{nl} net: {self.net}{nl}{cl}'