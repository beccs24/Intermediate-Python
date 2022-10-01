from Shape2D import Shape2D

class Circle(Shape2D):
    def __init__(self, color, radius):
        Shape2D.__init__(self, color)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def computeArea(self):
        return 3.14159 * (self.radius ** 2)

    def computePerimeter(self):
        return (2 * 3.14159 * self.radius)

    def getShapeProperties(self):
        return f'Shape: CIRCLE, Color: {self.getColor()}, Radius: {self.getRadius()}, Area: {self.computeArea()}, Perimeter: {self.computePerimeter()}'


c1 = Circle("blue", 2.5)
# print(c1.getShapeProperties())
