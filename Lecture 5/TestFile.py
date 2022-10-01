from Lecture5 import biggestInt

# imports the biggestInt function from Lecture5.py

def test_biggestInt1():
    assert biggestInt(1, 2, 3, 4) == 4
    assert biggestInt(1, 2, 4, 3) == 4
    assert biggestInt(1, 4, 2, 4) == 4

def test_biggestInt2():
    assert biggestInt(5, 5, 5, 5) == 5

def test_biggestInt3():
    assert biggestInt(-5, -10, -12, -100) == -5
    assert biggestInt(-100, 1, 100, 0) == 100
