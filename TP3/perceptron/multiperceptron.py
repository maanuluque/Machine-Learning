from math import copysign
import numpy as np
from numpy import ndarray 

class Layer:
    def __init__(self, neurons_amount, input_amount, activation_deriv):
        self.activation_deriv = activation_deriv
        # Weights matrix, each row represents each neurons weights
        self.weights = np.random.rand(neurons_amount, input_amount)*2 - 1
        # Arrays with each neurons information (input/output/activation/error)
        self.inputs = None
        self.outputs = None
        self.activations = None
        self.errors = None
        
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
    def __init__(self, activation_func, activation_deriv, learning_rate: float, beta: float, layers: int, layer_dims: list, data_dim: int):   
        # Array of layers, each layers input is previous layers dimension
        layer_list = list()
        prev_dim = data_dim
        for dim in layer_dims:
            layer_list.append(Layer(dim, prev_dim, activation_deriv))
            prev_dim = dim
        self.layers = np.array(layer_list)
        self.learning_rate: float = learning_rate
        self.beta = beta        
        self.activation_func = activation_func
        self.activation_deriv = activation_deriv

    # Predict output for a given point coordenates (inputs)
    def predict(self, inputs: ndarray):
        layer_inputs = inputs
        for layer in self.layers:
            layer.inputs = layer_inputs
            layer.outputs = layer.weights.dot(layer.inputs)
            layer.activations = self.activation_func(self.beta*layer.outputs)
            layer_inputs = layer.activations
        return layer_inputs

    # Train weights with output for a given point coordenates (inputs)
    def train(self, inputs: ndarray, expected: float):
        predicted: float = self.predict(inputs)
        self.propagate_error(expected, predicted)
        self.update_weights()

    def predict_list(self, point_list: ndarray):
        predicted_list: ndarray = np.zeros(point_list.shape[0])
        for idx, point in enumerate(point_list):
            predicted_list[idx] = self.predict(point)
        return predicted_list

    def train_list(self, point_list: ndarray, expected_list: ndarray):
        for idx, point in enumerate(point_list):
            self.train(point, expected_list[idx])

    # Propagate backwards, first input_error equals final total perceptron error
    def propagate_error(self, expected, predicted):
        # reverse layers array for backpropagation
        reversed_layers = np.flip(self.layers, 0)
        final_layer = reversed_layers[0]
        final_error = (expected-predicted) * self.beta * self.activation_deriv(predicted)
        final_layer.errors = final_error
        prev_errors = final_layer.calculate_errors()
        # Skip first layer (final perceptron layer)
        for layer in reversed_layers[1:]:
            layer.errors = prev_errors
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