from Car import *
from CarInventoryNode import *
from CarInventory import *

def testCar():
    # test __init__
    c1 = Car("Honda", "CRV", 2007, 8000)
    c2 = Car("Nissan", "Leaf", 2018, 18000)
    c3 = Car("Tesla", "Model3", 2018, 50000)
    c4 = Car("Mercedes", "Sprinter", 2022, 40000)
    c5 = Car("Mercedes", "Sprinter", 2014, 25000)
    c6 = Car("Ford", "Ranger", 2021, 25000)
    c7 = Car("Ford", "Ranger", 2021, 25000)
    c8 = Car("Ford", "Ranger", 2021, 30000)

    # test __gt__
    assert (c3 > c1) == True
    assert (c4 > c5) == True
    assert (c7 > c8) == False
    assert (c6 > c7) == False

    # test __lt__
    assert (c1 < c2) == True
    assert (c5 < c4) == True
    assert (c8 < c6) == False
    assert (c3 < c4) == False

    # test __eq__
    assert (c1 == c2) == False
    assert (c6 == c7) == True

    # test __str__ 
    c = Car("Honda", "CRV", 2007, 8000)
    assert str(c) == 'Make: HONDA, Model: CRV, Year: 2007, Price: $8000'


def testCarInventoryNode():
    # test __init__
    car1 = Car("Honda", "CRV", 2007, 8000)
    car2 = Car("Nissan", "Leaf", 2018, 18000)
    car3 = Car("Tesla", "Model3", 2018, 50000)
    car4 = Car("Mercedes", "Sprinter", 2022, 40000)
    
    carNode1 = CarInventoryNode(car1)
    carNode2 = CarInventoryNode(car2)
    carNode3 = CarInventoryNode(car3)
    carNode4 = CarInventoryNode(car4)

    # test getMake
    assert carNode1.getMake() == 'HONDA'
    assert carNode2.getMake() == 'NISSAN'
    assert carNode3.getMake() == 'TESLA'
    assert carNode4.getMake() == 'MERCEDES'

    # test getModel
    assert carNode1.getModel() == 'CRV'
    assert carNode2.getModel() == 'LEAF'
    assert carNode3.getModel() == 'MODEL3'
    assert carNode4.getModel() == 'SPRINTER'

    # test getParent
    assert carNode1.getParent() == None
    assert carNode2.getParent() == None
    assert carNode3.getParent() == None
    assert carNode4.getParent() == None

    # test setParent
    carNode1.setParent(carNode2)
    carNode4.setParent(carNode1)
    assert carNode1.getParent() == carNode2
    assert carNode2.getParent() == None
    assert carNode3.getParent() == None
    assert carNode4.getParent() == carNode1
    
    # test getLeft
    assert carNode1.getLeft() == None
    assert carNode2.getLeft() == None
    assert carNode3.getLeft() == None
    assert carNode4.getLeft() == None

    # test setLeft
    carNode1.setLeft(carNode4)
    assert carNode1.getLeft() == carNode4
    
    # test getRight
    assert carNode1.getRight() == None
    assert carNode2.getRight() == None
    assert carNode3.getRight() == None
    assert carNode4.getRight() == None

    # test setRight
    carNode1.setRight(carNode3)
    assert carNode1.getRight() == carNode3

    # test __str__
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)

    assert str(carNode) == 'Make: DODGE, Model: DART, Year: 2015, Price: $6000\
\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n'


def testCarInventory():
    # test __init__
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    car6 = Car("Ford", "Leaf", 2003, 21000)

    bst = CarInventory()

    # test addCar
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    # test doesCarExist
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car2) == True
    assert bst.doesCarExist(car3) == True
    assert bst.doesCarExist(car4) == True
    assert bst.doesCarExist(car5) == True
    assert bst.doesCarExist(car6) == False

    # test inOrder
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    
    # test preOrder
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    # test postOrder
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""

    # test getBestCar
    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    # test getWorstCar
    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None
    
    # test getTotalInventoryPrice
    assert bst.getTotalInventoryPrice() == 158000
