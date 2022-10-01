from Shape2D import Shape2D

class Square(Shape2D):
    def __init__(self, color, side):
        Shape2D.__init__(self, color)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        return self.side ** 2

    def computePerimeter(self):
        return self.side * 4

    def getShapeProperties(self):
        return f"Shape: SQUARE, Color: {self.getColor()}, Side: {self.getSide()}, Area: {self.computeArea()}, Perimeter: {self.computePerimeter()}"

s1 = Square("blue", 2.5)
# print(s1.getShapeProperties())
