from Car import *
from CarInventoryNode import *
from CarInventory import *


def test_getSuccessor():
    # test __init__
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    # Case 1: node does not exist
    assert bst.getSuccessor('Mazda', 'CX-4') == None

    # Case 2: node has right child
    assert bst.getSuccessor('Mazda', 'CX-5') == CarInventoryNode(car2)

    # Case 3: node has no right child but has a parent
    assert bst.getSuccessor('BMW', 'X5') == CarInventoryNode(car1)
    assert bst.getSuccessor('Audi', 'A3') == CarInventoryNode(car3)
    assert bst.getSuccessor('Tesla', 'Model3') == None


def test_inOrderRemove():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    
    #                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
    #                                 /                                       \
    #           BMW,X5,[Car(BMW,X5,2022,60000),Car(BMW,X5,2020,58000)]    Tesla,Model3,[Car(Tesla, Model3,2018,50000)]
    #                   /
    #  Audi,A3,[Car(Audi,A3,2021,25000)]


    # Case 0: car exists in node list and length of list is not 0 after removal (node is not removed)
    assert bst.removeCar("BMW", "X5", 2020, 58000) == True
    bst.removeCar("BMW", "X5", 2020, 58000)

    #                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
    #                                 /                                       \
    #           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
    #                   /
    #  Audi,A3,[Car(Audi,A3,2021,25000)]

    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    # Case 2: node has one child
    bst.removeCar("BMW", "X5", 2022, 60000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]

    assert bst.removeCar("BMW", "X5", 2022, 60000) == False
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    # Case 1: node has no children
    bst.removeCar("Tesla", "Model3", 2018, 50000)
    
    assert bst.removeCar("Tesla", "Model3", 2018, 50000) == False
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""
    

def test_preOrderRemove():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    

    bst.removeCar("BMW", "X5", 2020, 58000)

    #                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
    #                                 /                                       \
    #           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
    #                   /
    #  Audi,A3,[Car(Audi,A3,2021,25000)]


    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    bst.removeCar("BMW", "X5", 2022, 60000)

    #                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
    #                                 /                                       \
    #           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]


    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    # Case 3: node has both children
    bst.removeCar('Mazda', 'CX-5', 2022, 25000)
    
    assert bst.preOrder() == \
"""\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
"""

def test_postOrderRemove():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)


    bst.removeCar("BMW", "X5", 2020, 58000)

    #                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
    #                                 /                                       \
    #           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
    #                   /
    #  Audi,A3,[Car(Audi,A3,2021,25000)]

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

    bst.removeCar("BMW", "X5", 2022, 60000)

    #                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
    #                                 /                                       \
    #           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3[Car(Tesla,Model3,2018,50000)]


    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

    bst.removeCar("Audi", "A3", 2021, 25000)

    assert bst.postOrder() == \
"""\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

    bst.removeCar('Tesla', 'Model3', 2018, 50000)

    assert bst.postOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

    bst.removeCar('MAZDA', 'CX-5', 2022, 25000)

    assert bst.postOrder() == ''
