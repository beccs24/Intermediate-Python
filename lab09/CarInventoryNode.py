from Car import *

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.parent = None
        self.left = None
        self.right = None
        self.cars = []
        self.cars.append(car)

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

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


    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def replaceNodeData(self, make, model, cars, lc, rc):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self
          

    def __eq__(self, rhs):
        if rhs == None:
            return False
        else:
            if self.make == rhs.make and self.model == rhs.model:
                return True

    def __gt__(self, rhs):            
        if self.make > rhs.make:
            return True
        elif self.make < rhs.make:
            return False
        else:
            if self.model > rhs.model:
                return True
            else:
                return False
        
    def __lt__(self, rhs):
        if self.make > rhs.make:
            return False
        elif self.make < rhs.make:
            return True
        else:
            if self.model >= rhs.model:
                return False
            else:
                return True
            
    def findMin(self):
        current = self
        while current.getLeft() != None:
            current = current.getLeft()
        return current
