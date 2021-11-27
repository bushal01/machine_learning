import numpy as np

class Optimizer:
    def __init__(self, loss_function, estimator):
        self.loss_function = loss_function
        self.estimator = estimator

    def optimize(self):
        raise NotImplementedError("optimize must be implemented and called from the subclass")


class GradientDescent(Optimizer):
    def __init__(self, loss_function, estimator, gradient_function):
        super().__init__(loss_function, estimator)
        self.gradient_function = gradient_function

    def optimize(self, X, y, learning_rate, epsilon):
        previous_weights = []
        current_weights = []
        convergence_estimate = epsilon + 1
        while convergence_estimate > epsilon:
            current_weights = previous_weights + learning_rate * self.gradient_function(X, y)
            convergence_estimate = []
        return


def euclidean_distance(x, y):
    return