from Car import *
from CarInventoryNode import *

class CarInventory:
    
    def __init__(self):
        self.root = None 


    def addCar(self, car):
        if self.root:
            carNode = CarInventoryNode(car)
            self._put(carNode, self.root)
        else:
            self.root = CarInventoryNode(car)
        
    def _put(self, carNode, currentNode):
        if carNode == currentNode:
            currentNode.cars.append(carNode.cars[0])
            
        elif carNode < currentNode:
            if currentNode.getLeft() != None:
                self._put(carNode, currentNode.getLeft())
            else:
                currentNode.setLeft(carNode)
                carNode.setParent(currentNode)
                
        elif carNode > currentNode:
            if currentNode.getRight() != None:
                self._put(carNode, currentNode.getRight())
            else:
                currentNode.setRight(carNode)
                carNode.setParent(currentNode)
        
            


    def doesCarExist(self, car):
        if self.root:
            res = self._get(car, self.root)
            if res:
                for i in res.cars:
                    if i == car:
                        return True
        return False

    def _get(self, car, currentNode): 
        node = CarInventoryNode(car)
        if not currentNode:
            return None
        elif node < currentNode:
            return self._get(car, currentNode.getLeft())
        elif node > currentNode:
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


    def getSuccessor(self, make, model):
        car = Car(make, model, 0, 0)
        res = self._get(car, self.root)
        succ = None
        if res:
            if res.right:
                succ = res.right.findMin()
            else:
                if res.getParent():
                    parent_node = res.getParent()
                    while parent_node:
                        if parent_node > res:
                            return parent_node
                        parent_node = parent_node.getParent()
                    succ = parent_node
        return succ


    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        res = self._get(car, self.root)

        found = False
        if self.doesCarExist(car) == False:
            return False
        else:
            for c in res.cars:
                if c == car:
                    found = True
                    res.cars.remove(c)
                    break
            if not found:
                return False
        if res and car:
            if len(res.cars) == 0:
                if res.isLeaf():
                    if res.isRoot():
                        res = None
                    elif res == res.parent.left:
                        res.parent.left = None
                    elif res == res.parent.right:
                        res.parent.right = None
                        
                elif res.hasBothChildren():
                    succ = self.getSuccessor(make, model)
                    succ.spliceOut()
                    res.make = succ.make
                    res.model = succ.model
                    res.cars = succ.cars

                else:
                    if res.hasLeftChild():
                        if res.isLeftChild():
                            res.left.parent = res.parent
                            res.parent.left = res.left
                        elif res.isRightChild():
                            res.left.parent = res.parent
                            res.parent.right = res.left
                        else:
                            res.replaceNodeData(res.left.make,
                                                res.left.model,
                                                res.left.cars,
                                                res.left.left,
                                                res.left.right)
                    else:
                        if res.isLeftChild():
                            res.right.parent = res.parent
                            res.parent.left = res.right
                        elif res.isRightChild():
                            res.right.parent = res.parent
                            res.parent.right = res.right
                        else:
                            res.replaceNodeData(res.right.make,
                                                res.right.model,
                                                res.right.cars,
                                                res.right.left,
                                                res.right.right)
        return True

'''
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove) # remove modifies the tree
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
'''
