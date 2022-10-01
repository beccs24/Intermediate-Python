from Shape2D import Shape2D
from Circle import Circle
from Square import Square


def test_Shape2D():
    # test getColor()
    # test initial constructor
    s1 = Shape2D("blue")
    assert s1.getColor() == 'blue'

    # test setColor()
    s1.setColor('green')
    assert s1.getColor() == 'green'

    # test getShapeProperties()
    s1.getShapeProperties()
    assert s1.getShapeProperties() == 'Shape: N/A, Color: green'


def test_Circle():
    # test getRadius()
    # test initial constructor
    s2 = Circle('purple', 2.5)
    assert s2.getColor() == 'purple'
    assert s2.getRadius() == 2.5

    # test setRadius()
    s2.setRadius(4)
    assert s2.getRadius() == 4

    # test computeArea()
    s2.computeArea()
    assert s2.computeArea() == 50.26544

    # test computePerimeter()
    s2.computePerimeter()
    assert s2.computePerimeter() == 25.13272

    # test getShapeProperties()
    s2.getShapeProperties()
    assert s2.getShapeProperties() == 'Shape: CIRCLE, Color: purple, \
Radius: 4, Area: 50.26544, Perimeter: 25.13272'
    

def test_Square():
    # test getSide()
    # test initial constructor
    s3 = Square('teal', 5.3)
    assert s3.getColor() == 'teal'
    assert s3.getSide() == 5.3

    # test setSide()
    s3.setSide(100)
    assert s3.getSide() == 100

    # test computeArea()
    s3.computeArea()
    assert s3.computeArea() == 10000

    # test computePerimeter()
    s3.computePerimeter()
    assert s3.computePerimeter() == 400

    # test getShapeProperties()
    s3.getShapeProperties()
    assert s3.getShapeProperties() == 'Shape: SQUARE, Color: teal, Side: 100, \
Area: 10000, Perimeter: 400'
