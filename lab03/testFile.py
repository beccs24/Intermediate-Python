from lab03 import *

def integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(10, 5) == 2
    assert integerDivision(1, 5) == 0
    assert integerDivision(12, 12) == 1
    assert integerDivision(0, 15) == 0


def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([1,3,5]) == []
    assert collectEvenInts([2]) == [2]
    assert collectEvenInts([2,10,2003]) == [2, 10]


def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("") == 0
    assert countVowels("Hi") == 1
    assert countVowels("cool!") == 2
    assert countVowels("rhythm") == 0
    

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("dog") == "god"
    assert reverseString("R") == "R"
    assert reverseString("RACE CAR") == "RAC ECAR"


def test_removeSubString():
    # The first "lol" is removed, which reduces the string 
    # to: "Loolol". Then the 2nd "lol" is removed, which 
    # reduces the string to: "Loo"
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("Hi", "i") == "H"
    assert removeSubString("", "") == ""
    assert removeSubString("hi", "lol") == "hi"
    assert removeSubString("str", "lol") == "str"
    assert removeSubString("cool", "cool") == ""

