from Apartment import *
from lab06 import *

def testApartment():
    # test __init__
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")


    # test getRent, getMetersFromUCSB, getCondition
    assert a0.getRent() == 1115
    assert a0.getMetersFromUCSB() == 215
    assert a0.getCondition() == 'bad'

    assert a5.getRent() == 500
    assert a5.getMetersFromUCSB() == 250
    assert a5.getCondition() == 'bad'


    # test getApartmentDetails
    a6 = Apartment(1204, 200, "bad")
    assert a6.getApartmentDetails() == '(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad'
    assert a3.getApartmentDetails() == '(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent'


    # test __gt__
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")

    assert (a0 > a5) == True
    assert (a1 > a2) == True
    assert (a4 > a2) == False
    assert (a3 > a1) == False

    
    # test __eq__
    assert (a5 == a5) == True
    assert (a1 == a4) == False
    

    # test __lt__
    assert (a5 < a0) == True
    assert (a3 < a1) == True
    assert (a2 < a4) == False
    assert (a4 < a4) == False
    

def test_lab06():
    # test ensureSortedAscending, mergesort
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert apartmentList == [a5, a4, a3, a2, a1, a0]
    assert ensureSortedAscending(apartmentList) == True


    # test getBestApartment, getWorstApartment
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    assert getBestApartment(apartmentList) == '(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad'
    assert getWorstApartment(apartmentList) == '(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average'


    # test getAffordableApartments
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getAffordableApartments(apartmentList, 450) == ''
    assert getAffordableApartments(apartmentList, 950) == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n\
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average'
    
