import math
class Perceptron():

    def __init__(self, weight, inputs, bias):
        self.w = weight
        self.x = inputs
        self.b = bias
        self.z = 0
        self.out = 0
        self.calculateZ()
        self.sigmoid()

    def sigmoid (self):
        a = 1 + math.e ** - self.z
        self.out = 1 / a


    def calculateZ(self):
        print(len(self.x))
        for i in range(len(self.x)):
            self.z = self.z + (self.x[i] * self.w[i])

        print(self.z)
        self.z = self.z + self.b

    def printValues(self):
        print("The input is ")
        print(self.x)
        print("The weight is ")
        print(self.w)
        print("The bias is  ")
        print(self.b)
        print("The z is")
        print(self.z)
        print("The output is")
        print(self.out)


if __name__ == '__main__':
    neuron = Perceptron([1,1],[0,1], 1)
    neuron.printValues()





