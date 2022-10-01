from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *

class PizzaOrder:
    def __init__(self, time):
        self.pizza = []
        self.time = time

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizza.append(pizza)

    def getOrderDescription(self):
        orderString = ''
        orderString += f'******\nOrder Time: {self.time}\n'

        totalPrice = 0
        
        for i in range(len(self.pizza)):
            orderString += self.pizza[i].getPizzaDetails() + '\n----\n'
            totalPrice += self.pizza[i].getPrice()

        orderString += f'TOTAL ORDER PRICE: ${totalPrice:.2f}\n' + '******\n'       
        return orderString
