from math import copysign
import numpy as np
from numpy import ndarray 

class SimplePerceptron:
    def __init__(self, weights: ndarray, learning_rate: float):   
        self.weights: ndarray = weights
        self.learning_rate: float = learning_rate

    def predict(self, point: ndarray):
        h: float = self.weights.dot(point)
        return copysign(1, h)
    
    def train(self, point: ndarray, expected: float):
        predicted: float = self.predict(point)
        delta_w = self.learning_rate * (expected - predicted) * point
        self.weights += delta_w 

    def predict_list(self, point_list: ndarray):
        predicted_list: ndarray = np.zeros(point_list.size)
        for idx, point in enumerate(point_list):
            predicted_list.put(idx, self.predict(point))
        return predicted_list
            
    def train_list(self, point_list: ndarray, expected_list: ndarray):
        for idx, point in enumerate(point_list):
            self.train(point, expected_list[idx])

    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl} weights: {self.weights}{nl} rate: {self.learning_rate}{nl}{cl}'
