# this will use a neural network to predict the grades that a student will get based on hours studied and sleep
# https://medium.com/dair-ai/a-simple-neural-network-from-scratch-with-pytorch-and-google-colab-c7f3830618e0

import torch
import torch.nn as nn

x = torch.tensor(([2,9],[1,5],[3,6]),  dtype=torch.float)
y = torch.tensor(([92], [100], [89]), dtype=torch.float)
xPredicted = torch.tensor(([4, 8]), dtype=torch.float)

print(x.size())

# scaling so we have decimal values, largest is 1 and smallest is 0
xMax, _ = torch.max(x, 0)
x = torch.div(x, xMax)
y = y/100

class NeuralNetwork(nn.Module):
    def __init__(self, ):
        super(NeuralNetwork, self).__init__()

        self.outputSize = 1
        self.inputSize = 2
        self.hiddenSize = 3

        # these are the weights, or inner node values
        self.W1 = torch.randn(self.inputSize, self.hiddenSize)
        self.W2 = torch.randn(self.hiddenSize, self.outputSize)

    # this function performs a step which multiplies the values with the weights, and gets a result
    def forward(self, X):
        self.z = torch.matmul(X, self.W1) # 3 X 3 ".dot" does not broadcast in PyTorch
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = torch.matmul(self.z2, self.W2)
        o = self.sigmoid(self.z3) # final activation function
        return o
        
    def sigmoid(self, s):
        print('SIGMOID')
        print(s)
        print(1 / (1 + torch.exp(-s)))
        return 1 / (1 + torch.exp(-s))
    
    def sigmoidPrime(self, s):
        # derivative of sigmoid
        print(s)
        print(s*(1-s))
        return s * (1 - s)
    
    # this function is what takes the output and changes the weights so we don't lose as much
    def backward(self, X, y, o):
        self.o_error = y - o # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o) # derivative of sig to error
        self.z2_error = torch.matmul(self.o_delta, torch.t(self.W2))
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += torch.matmul(torch.t(X), self.z2_delta)
        self.W2 += torch.matmul(torch.t(self.z2), self.o_delta)
        
    def train(self, X, y):
        # forward + backward pass for training
        o = self.forward(X)
        self.backward(X, y, o)
        
    def saveWeights(self, model):
        # we will use the PyTorch internal storage functions
        torch.save(model, "NN")
        # you can reload model with all the weights and so forth with:
        # torch.load("NN")
        
    def predict(self):
        print ("Predicted data based on trained weights: ")
        print ("Input (scaled): \n" + str(xPredicted))
        print ("Output: \n" + str(self.forward(xPredicted)))

NN = NeuralNetwork()
torch.mean((y - NN(x))**2).detach().item()
for i in range(1000):  # trains the NN 1,000 times
    print ("#" + str(i) + " Loss: " + str(torch.mean((y - NN(x))**2).detach().item()))  # mean sum squared loss
    NN.train(x, y)
NN.saveWeights(NN)
NN.predict()