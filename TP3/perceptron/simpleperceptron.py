from math import copysign
import numpy as np
from numpy import ndarray 

class SimplePerceptron:
    def __init__(self, weights: ndarray, learning_rate: float, beta: float, prediction_method: str):   
        self.weights: ndarray = weights
        self.learning_rate: float = learning_rate
        self.beta = beta
        if prediction_method == "step":
            self.prediction_method = self.step_function
            self.calculate_delta_w = self.linear_delta_w
        elif prediction_method == "linear":
            self.prediction_method = self.linear_function
            self.calculate_delta_w = self.linear_delta_w
        elif prediction_method == "tanh":
            self.prediction_method = self.tanh_function
            self.calculate_delta_w = self.tanh_delta_w
        elif prediction_method == "sigmoid":
            self.prediction_method = self.sigmoid_function
            self.calculate_delta_w = self.sigmoid_delta_w

    def predict(self, point: ndarray):
        h: float = self.weights.dot(point)
        return self.prediction_method(h)

    def train(self, point: ndarray, expected: float):
        predicted: float = self.predict(point)
        delta_w = self.calculate_delta_w(expected, predicted, point)
        self.weights += delta_w 
        self.weights = self.weights / np.linalg.norm(self.weights)

    def predict_list(self, point_list: ndarray):
        predicted_list: ndarray = np.zeros(point_list.shape[0])
        for idx, point in enumerate(point_list):
            predicted_list[idx] = self.predict(point)
        return predicted_list

    def train_list(self, point_list: ndarray, expected_list: ndarray):
        for idx, point in enumerate(point_list):
            self.train(point, expected_list[idx])

    def step_function(self, h):
        return copysign(1, h)

    def linear_function(self, h):
        return h

    def tanh_function(self, x):
        return np.math.tanh(self.beta * x)

    def sigmoid_function(self, x):
        exp = 2 * self.beta * -x
        ret = 1 / (1 + np.math.exp(exp))
        return ret

    def linear_delta_w(self, expected, predicted, point):
        return self.learning_rate * (expected - predicted) * point

    def tanh_delta_w(self, expected, predicted, point):
        deriv = self.beta * (1 - np.math.pow(self.tanh_function(predicted), 2))
        return self.learning_rate * (expected - predicted) * deriv * point

    def sigmoid_delta_w(self, expected, predicted, point):
        deriv = 2 * self.beta * self.sigmoid_function(predicted) * (1 - self.sigmoid_function(predicted)) 
        ret = self.learning_rate * (expected - predicted) * deriv * point
        return ret

    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl} weights: {self.weights}{nl} rate: {self.learning_rate}{nl}{cl}'
