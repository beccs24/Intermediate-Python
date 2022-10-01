from Pizza import *

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        
        if self.size == 'S':
            self.price = 8
        elif self.size == 'M':
            self.price = 10
        elif self.size == 'L':
            self.price = 12

        self.toppingsList = []

    def addTopping(self, topping):
        self.toppingsList.append(topping)
        
        if self.size == 'S':
            self.price += 0.5
        elif self.size == 'M':
            self.price += 0.75
        elif self.size == 'L':
            self.price += 1

    def getPizzaDetails(self):
        pizzaString = ''
        pizzaString += f'CUSTOM PIZZA\nSize: {self.size}\nToppings:\n'

        for i in range(len(self.toppingsList)):
            pizzaString += '\t+ ' + str(self.toppingsList[i]) + '\n'

        pizzaString += f'Price: ${self.price:.2f}\n'
        
        return pizzaString
        
