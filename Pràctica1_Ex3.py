import math
import numpy
class Perceptron2():

    def __init__(self,width, inputs, bias, start):
        self.w = numpy.array(width)
        self.x = numpy.array(inputs)
        self.b = bias
        self.z = 0
        self.out = 0
        if start == 1:
            self.calculateZ()
        if start == 0:
            self.calculateZ2()
        if start == 2:
            self.calculateZ3()
        self.sigmoid()

    def sigmoid (self):
        a = 1 + math.e ** - self.z
        self.out = 1 / a


    def calculateZ(self):
        z2 = self.z + (self.w.T.dot(self.x))
        self.z = z2 + self.b

    def calculateZ2(self):
        z2 = self.z + (self.w.dot(self.x))
        self.z = z2 + self.b

    def calculateZ3(self):
        z2 = self.z + (self.w.T.dot(self.x))
        self.z = z2 + self.b

    def printValues(self):
        print("The input is ")
        print(self.x)
        print("The weight is ")
        print(self.w.T)
        print("The bias is  ")
        print(self.b)
        print("The z is")
        print(self.z)
        print("The output is")
        print(numpy.matrix.round(self.out))

    def printOutput(self):
        print(numpy.matrix.round(self.out))

    def getA(self):
        return self.out
    def getW(self):
        return self.w
    def getB(self):
        return self.b
    def calculateNewWeightEnd(self, rate, expected, transort):
        if transort == 1:
            W2 = self.w.T - rate * (self.out - expected)
        else:
            W3 = self.w
            W2 = W3 - rate * (self.out - expected)
        return W2
    def calculateNewBiasEnd(self, rate, expected):
        B2 = self.b - rate * (self.out - expected)
        return B2
    def calculateD(self, expected, weight, A):
        D = (weight * (self.out - expected)).dot(A.dot(1-A))
        return D
if __name__ == '__main__':

    print("El resultat de la dreta es la porta XOR i el de l'esquerra es la porta AND")
    j = 0
    while j < 4:
        a = 0.25
        W = ([1,1,1],[1,1,1])
        B = 1
        match j:
            case 0:
                Y = (0,0)
                X = (0,0)
            case 1:
                Y = (0, 1)
                X = (0, 1)
            case 2:
                Y = (0, 1)
                X = (1, 0)
            case 3:
                Y = (1,0)
                X = (1,1)

        neuron = Perceptron2(W, X, B, 1)
        A1 = neuron.getA()
        neuron2 = Perceptron2(W, A1, B, 0)
        W2 = neuron2.calculateNewWeightEnd(a, Y, 1)
        B2 = neuron2.calculateNewBiasEnd(a, Y)
        D = neuron2.calculateD(Y, W2, A1)
        W4 = neuron.getW()
        Aux = numpy.array(a * D)
        W5 = W4 - Aux.T
        B3 = neuron.getB() - a * D[0]
        i = 1
        while i < 15000:

            neuron = Perceptron2(W5, X, B3[0], 1)
            A1 = neuron.getA()
            A2 = numpy.array(A1)
            if(i%2 != 0):
                neuron2 = Perceptron2(W2, A2.T, B2 , 2)
                W2 = neuron2.calculateNewWeightEnd(a, Y, 0)
                B2 = neuron2.calculateNewBiasEnd(a, Y)
                D = neuron2.calculateD(Y, W2, A1)
                W4 = neuron.getW()
                Aux = numpy.array(a * D)
                W5 = W4 - Aux.T
                B3 = neuron.getB() - a * D[0]
            else:
                neuron2 = Perceptron2(W2, A2.T, B2, 2)
                W2 = neuron2.calculateNewWeightEnd(a, Y, 0)
                B2 = neuron2.calculateNewBiasEnd(a, Y)
                D = neuron2.calculateD(Y, W2, A1)
                W4 = neuron.getW()
                Aux = numpy.array(a * D)
                W5 = W4 - Aux.T
                B3 = neuron.getB() - a * D[0]


            i = i + 1

        neuron2.printOutput()
        j = j + 1

