from Car import *

class CarInventoryNode:
    def __init__(self, car):
        self.car = car
        self.car.make = car.make.upper()
        self.car.model = car.model.upper()
        self.parent = None
        self.left = None
        self.right = None
        self.cars = []
        self.cars.append(car)

    def getMake(self):
        return self.car.make

    def getModel(self):
        return self.car.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        string = ""
        for i in self.cars:
            string += str(i) + '\n'
        return string
