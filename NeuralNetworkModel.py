import numpy as np


class NeuralNetwork(object):

    def __init__(self):
        self.a1 = None
        self.z1 = None
        self.a2 = None
        self.y = None
        self.w1 = np.array([[0.8,0.4,0.3],[0.2,0.9,0.5]])
        self.w2 = np.array([[0.3], [0.5], [0.9]])

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def sigmoid_prime(z):
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def forward(self, x): # x should by a (1, 1) dimension array
        self.a1 = np.dot(x, self.w1)
        self.z1 = self.sigmoid(self.a1)

        self.a2 = np.dot(self.z1, self.w2)
        self.z2 = self.sigmoid(self.a2)

        self.y = self.z2
        return self.y

    def margin_error(self, x, y):
        return y - self.forward(x)

    def delta_output_sum(self, x, y):
        return self.sigmoid_prime(NN.a2) * (self.margin_error(x, y))

    def delta_hidden_sum_a1(self, x, y):
        sigp_a1 = self.sigmoid_prime(self.a1)
        quotient_dos_w2 = self.delta_output_sum(x, y) / self.w2
        delta_hidden_sum = np.dot(quotient_dos_w2, sigp_a1)
        return np.array([[delta_hidden_sum[0][0]], [delta_hidden_sum[1][1]], [delta_hidden_sum[2][2]]])

    def delta_weights(self, x, y):
        dw2 = self.delta_output_sum(x, y) / self.z1
        dw1 = self.delta_hidden_sum_a1(x, y) / x


        return dw1, dw2

    def train(self, x, y, iterations=1000):
        epochs = 0

        for i in range(iterations):
            dw1, dw2 = self.delta_weights(x, y)
            dw1 = dw1.ravel().reshape(2, 3)
            dw2 = dw2.ravel().reshape(3, 1)
            self.w1 += dw1
            self.w2 += dw2
            epochs += 1

        return epochs

# Test code
x = np.array([[1, 1]])
y = np.array([[0.89]])
NN = NeuralNetwork()
print(NN.forward(x))
print(NN.train(x,y))
print(NN.forward(x))

