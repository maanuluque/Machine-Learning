import math
from math import copysign
import numpy as np
from numpy import ndarray
from scipy.optimize import minimize
import functools

class Layer:
    @staticmethod
    def new(neurons_amount, input_amount, activation_deriv):
        layer = Layer()
        layer.activation_deriv = activation_deriv
        # Weights matrix, each row represents each neurons weights
        layer.weights = np.random.rand(neurons_amount, input_amount) * 2 - 1
        # Arrays with each neurons information (input/output/activation/error)
        layer.inputs = None
        layer.outputs = None
        layer.activations = None
        layer.errors = None
        layer.latent = False
        return layer

    @staticmethod
    def new_from_weights(weights, activation_deriv):
        layer = Layer()
        layer.weights = weights
        layer.activation_deriv = activation_deriv
        layer.inputs = None
        layer.outputs = None
        layer.activations = None
        layer.errors = None
        layer.latent = False
        return layer


    def calculate_errors(self):
        # Calculate previous layer errors
        errors = self.errors.dot(self.weights)[0] * self.activation_deriv(self.inputs)
        return errors

    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl}   weights: {self.weights}{nl}   inputs: {self.inputs}{nl}   activations: {self.activations}{nl}   errors: {self.errors}{nl}  {cl}{nl}'


class MultiPerceptron:
    @staticmethod
    def new(activation_func, activation_deriv, learning_rate: float, beta: float, layers: int,
                 layer_dims: list, data_dim: int):
        mp = MultiPerceptron()
        # Array of layers, each layers input is previous layers dimension
        layer_list = list()
        latent_layer = math.floor(layers / 2) + 1
        counter = 1
        prev_dim = data_dim
        layer_shapes = []
        for dim in layer_dims:
            layer_shapes.append((dim, prev_dim))
            layer = Layer.new(dim, prev_dim, activation_deriv)
            layer_list.append(layer)
            prev_dim = dim
            if counter == latent_layer:
                layer.latent = True
            counter = counter + 1
        mp.layers = np.array(layer_list)
        mp.learning_rate: float = learning_rate
        mp.beta = beta
        mp.activation_func = activation_func
        mp.activation_deriv = activation_deriv
        mp.layer_shapes = layer_shapes
        return mp


    @staticmethod
    def new_from_weights(weights: ndarray, activation_func, activation_deriv, learning_rate, beta):
        mp = MultiPerceptron()
        layer_list = list()
        latent_layer = math.floor(len(weights) / 2) + 1
        counter = 1
        for weight in weights:
            layer = Layer.new_from_weights(weight, activation_deriv)
            layer_list.append(layer)
            if counter == latent_layer:
                layer.latent = True
            counter = counter + 1
        mp.layers = np.array(layer_list)
        mp.learning_rate: float = learning_rate
        mp.beta = beta
        mp.activation_func = activation_func
        mp.activation_deriv = activation_deriv
        return mp

    
    @staticmethod
    def new_optimized(activation_func, activation_deriv, learning_rate: float, beta: float, layers: int,
                 layer_dims: list, data_dim: int, inputs, expected, options=None):
        mp = MultiPerceptron.new(activation_func, activation_deriv, learning_rate, beta, layers, layer_dims, data_dim)
        weights = []
        for layer in mp.layers:
            weights.append(layer.weights)
        weights = np.array(weights)
        def optimize(weights):
            weights = MultiPerceptron.reshape_weights(weights, mp.layer_shapes)
            perceptron = MultiPerceptron.new_from_weights(weights, activation_func, activation_deriv, learning_rate, beta)
            output = perceptron.predict_list(inputs)
            error_list = MultiPerceptron.cost(output, expected)
            expected_error = [0 for _ in error_list]
            error = MultiPerceptron.cost(error_list, expected_error)
            return error
        
        flat_weights = MultiPerceptron.flatten_weights(weights)
        flat_opt_weights = minimize(optimize, flat_weights, method='powell', options=options)
        opt_weights = MultiPerceptron.reshape_weights(flat_opt_weights.x, mp.layer_shapes)
        return MultiPerceptron.new_from_weights(opt_weights, activation_func, activation_deriv, learning_rate, beta)


    @staticmethod
    def reshape_weights(weights, dims):
        reshape = []
        offset = 0
        for dim in dims:
            amount = dim[0] * dim[1]
            w = weights[offset : offset+amount]
            reshape.append(w.reshape(dim[0], dim[1]))
            offset += amount
        return reshape

    @staticmethod
    def flatten_weights(weights):
        reshape = []
        for w in weights:
            w_flat = w.reshape(w.size)
            reshape.extend(w_flat)
        return np.array(reshape)

    def return_latent(self):
        for layer in self.layers:
            if layer.latent:
                return layer

    # Predict output for a given point coordenates (inputs)
    def predict(self, inputs: ndarray):
        inputs = np.array(inputs)
        layer_inputs = inputs
        for layer in self.layers:
            layer.inputs = layer_inputs
            layer.outputs = layer.weights.dot(layer.inputs)
            layer.activations = self.activation_func(self.beta * layer.outputs)
            layer_inputs = layer.activations
        return layer_inputs

    def predict_from_latent(self, inputs: ndarray):
        layer_inputs = inputs
        start = False
        for layer in self.layers:
            if layer.latent:
                start = True
            if start:
                layer.inputs = layer_inputs
                layer.outputs = layer.weights.dot(layer.inputs)
                layer.activations = self.activation_func(self.beta * layer.outputs)
                layer_inputs = layer.activations
        return layer_inputs

    # Train weights with output for a given point coordenates (inputs)
    def train(self, inputs: ndarray, expected: float):
        predicted: float = self.predict(inputs)
        self.propagate_error(expected, predicted)
        self.update_weights()

    def predict_list(self, point_list: ndarray):
        predicted_list = []
        for idx, point in enumerate(point_list):
            predicted_list.append(self.predict(point))
        return predicted_list

    def train_list(self, point_list: ndarray, expected_list: ndarray):
        for idx, point in enumerate(point_list):
            self.train(point, expected_list[idx])


    @staticmethod
    def cost(x, y):
        diff = x - y
        sum = 0
        for i in range(len(diff)):
            sum += (diff[i] ** 2)
        return sum / len(diff)

    # Propagate backwards, first input_error equals final total perceptron error
    def propagate_error(self, expected, predicted):
        # reverse layers array for backpropagation
        reversed_layers = np.flip(self.layers, 0)
        final_layer = reversed_layers[0]

        diff = (expected - predicted)
        final_error = diff * self.beta * self.activation_deriv(predicted)
        final_layer.errors = final_error
        prev_errors = final_layer.calculate_errors()
        # Skip first layer (final perceptron layer)
        for idx, layer in enumerate(reversed_layers[1:]):
            layer.errors = prev_errors
            if idx == (len(reversed_layers) - 2):
                break
            prev_errors = layer.calculate_errors()

    # Update weight values for each layer based on calculated errors
    def update_weights(self):
        for layer in self.layers:
            errors = np.array([layer.errors])
            inputs = np.array([layer.inputs])
            layer.weights += self.learning_rate * (errors.T * inputs)

    def str_layers(self):
        string = '[ \n'
        for layer in self.layers:
            string += "  " + layer.__str__()
        string += '\n ]'
        return string

    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl} layers: {self.str_layers()}{nl} rate: {self.learning_rate}{nl}{cl}'
