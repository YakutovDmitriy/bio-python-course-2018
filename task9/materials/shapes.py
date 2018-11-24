import math


class IncorrectShape(Exception):
    pass


class Shape(object):

    def __init__(self, color):
        ''' Initialize current shape with given color '''
        self.color = color

    def getarea(self):
        ''' Returns area of current shape '''
        pass

    def getperimeter(self):
        ''' Returns perimeter of current shape '''
        pass

    def getangles(self):
        ''' Returns list of angles of current shape in degrees '''
        pass

    def __str__(self):
        ''' Returns string representing current shape '''
        return '{0} shape of area {1}'.format(self.color.capitalize(), self.getarea())

    def checkpositive(self, number):
        ''' Checks if number is positive. Raises Error if not '''
        if number <= 0:
            raise IncorrectShape('Value {0} should be positive'.format(number))


class Circle(Shape):

    def __init__(self, color, radius):
        self.checkpositive(radius)
        super(Circle, self).__init__(color)
        self.radius = radius

    def getarea(self):
        return math.pi * self.radius**2

    def getperimeter(self):
        return 2 * math.pi * self.radius

    def getangles(self):
        return []


class Rectangle(Shape):

    def __init__(self, color, width, height):
        self.checkpositive(width)
        self.checkpositive(height)
        super(Rectangle, self).__init__(color)
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height

    def getperimeter(self):
        return 2 * (self.width + self.height)

    def getangles(self):
        return [90] * 4


class Square(Rectangle):

    def __init__(self, color, side):
        super(Square, self).__init__(color, side, side)


class Triangle(Shape):

    def __init__(self, color, a, b, c):
        super(Triangle, self).__init__(color)
        self.checkpositive(a)
        self.checkpositive(b)
        self.checkpositive(c)
        if max(a, b, c) * 2 > a + b + c:
            raise IncorrectShape('Triangles inequality {0}, {1}, {2}:'.format(a, b, c))
        self.a = a
        self.b = b
        self.c = c

    def getarea(self):
        p = self.getperimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def getperimeter(self):
        return self.a + self.b + self.c

    def getangles(self):
        def calcangle(a, b, c):
            return math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        a, b, c = self.a, self.b, self.c
        return [x * 180 / math.pi for x in (calcangle(a, b, c),
                                            calcangle(b, c, a),
                                            calcangle(c, a, b))]
