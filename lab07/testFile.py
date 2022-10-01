from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *
from PizzaOrder import *
from OrderQueue import *
import pytest

def testPizza():
    # test __init__
    pizza1 = Pizza('S')
    pizza2 = Pizza('M')
    assert pizza1.getPrice() == 0.0
    assert pizza1.getSize() == 'S'

    # test setPrice, getPrice
    pizza1.setPrice(9.0)
    assert pizza1.getPrice() == 9
    assert pizza2.getPrice() == 0.0
    
    # test setSize, getSize
    pizza1.setSize('L')
    assert pizza1.getSize() == 'L'
    assert pizza2.getSize() == 'M'
    
    
def testCustomPizza():
    # test __init__, addTopping
    cp1 = CustomPizza("S")
    assert cp1.getSize() == 'S'
    assert cp1.getPrice() == 8

    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    cp2.addTopping("sausage")
    assert cp2.getSize() == 'L'
    assert cp2.getPrice() == 14

    # test getPizzaDetails
    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    assert cp2.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"


def testSpecialtyPizza():
    # test __init__
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getSize() == "S"
    assert sp1.getPrice() ==12

    # test getPizzaDetails
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    

def testPizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")

    # test __init__, getTime, setTime
    order = PizzaOrder(123456) #12:30:00PM
    assert order.getTime() == 123456
    order.setTime(123000)
    assert order.getTime() == 123000

    # test addPizza
    order.addPizza(cp1)
    order.addPizza(sp1)

    # test getOrderDescription
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"


def testOrderQueue():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    
    order1 = PizzaOrder(123000) #12:30:00PM
    order2 = PizzaOrder(102513)

    order1.addPizza(sp1)
    order2.addPizza(cp1)

    # test __init__
    pizzaline = OrderQueue()
    pizzaline.currentSize == 0

    # test addOrder
    pizzaline.addOrder(order1)
    pizzaline.addOrder(order2)
    
    # test processNextOrder
    assert pizzaline.processNextOrder() == \
"******\n\
Order Time: 102513\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $14.00\n\
******\n"
    assert pizzaline.processNextOrder() == \
"******\n\
Order Time: 123000\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $12.00\n\
******\n"

    # test Exception
    with pytest.raises(QueueEmptyException):
        pizzaline.processNextOrder()

