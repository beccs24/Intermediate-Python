from Car import *
from CarInventoryNode import *

class CarInventory:
    
    def __init__(self):
        self.root = None 


    def addCar(self, car):
        if self.root:
            self._put(car, self.root)
        else:
            self.root = CarInventoryNode(car)
        
    def _put(self, car, currentNode):
        if car.make < currentNode.car.make:
            if currentNode.getLeft() != None:
                self._put(car, currentNode.left)
            else:
                currentNode.left = CarInventoryNode(car)
                currentNode = currentNode.left.getParent()
        elif car.make > currentNode.car.make:
            if currentNode.getRight() != None:
                self._put(car, currentNode.right)
            else:
                currentNode.right = CarInventoryNode(car)
                currentNode = currentNode.right.getParent()
        else:
            if car.model < currentNode.car.model:
                if currentNode.getLeft() != None:
                    self._put(car, currentNode.left)
                else:
                    currentNode.left = CarInventoryNode(car)
                    currentNode = currentNode.left.getParent()
            elif car.model > currentNode.car.model:
                if currentNode.getRight() != None:
                    self._put(car, currentNode.right)
                else:
                    currentNode.right = CarInventoryNode(car)
                    currentNode = currentNode.right.getParent()
            else:
                currentNode.cars.append(car)


    def doesCarExist(self, car):
        if self.root:
            res = self._get(car, self.root)
            if res:
                for i in res.cars:
                    if i == car:
                        return True
        return False

    def _get(self, car, currentNode): 
        if not currentNode:
            return None
        elif car.make < currentNode.car.make:               
            return self._get(car, currentNode.getLeft())
        elif car.make > currentNode.car.make:
            return self._get(car, currentNode.getRight())
        else:
            if car.model < currentNode.car.model:
                return self._get(car, currentNode.getLeft())
            elif car.model > currentNode.car.model:
                return self._get(car, currentNode.getRight())
            else:
                return currentNode

       
    def inOrder(self):
        return self.__inOrder(self.root)

    def __inOrder(self, currentNode):
        string = ""
        if currentNode != None:
            string += self.__inOrder(currentNode.getLeft())
            string += str(currentNode)
            string += self.__inOrder(currentNode.getRight())
        return string


    def preOrder(self):
        return self.__preOrder(self.root)

    def __preOrder(self, currentNode):
        string = ""
        if currentNode != None:
            string += str(currentNode)
            string += self.__preOrder(currentNode.getLeft())
            string += self.__preOrder(currentNode.getRight())
        return string


    def postOrder(self):
        return self.__postOrder(self.root)
    
    def __postOrder(self, currentNode):
        string = ""
        if currentNode != None:
            string += self.__postOrder(currentNode.getLeft())
            string += self.__postOrder(currentNode.getRight())
            string += str(currentNode)
        return string


    def getBestCar(self, make, model):
        car = Car(make, model, 0, 0)
        if self.root:
            res = self._get(car, self.root)
            if res:
                best = res.cars[0]
                for i in res.cars:
                    if i > best:
                        best = i
                return best
        return None


    def getWorstCar(self, make, model):
        car = Car(make, model, 0, 0)
        if self.root:
            res = self._get(car, self.root)
            if res:
                worst = res.cars[0]
                for i in res.cars:
                    if i < worst:
                        worst = i
                return worst
        return None


    def getTotalInventoryPrice(self):
        return self.__getTIP(self.root)

    def __getTIP(self, currentNode):
        price = 0
        if not currentNode:
            return price
        elif currentNode:
            for i in currentNode.cars:
                price += i.price
            price += self.__getTIP(currentNode.getLeft())
            price += self.__getTIP(currentNode.getRight())
        return price
