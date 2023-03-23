import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x  # Tọa độ tung
        self.y = y  # Tọa độ hoành
        self.r = r

    def getPerimeter(self):  # Chu vi
        return 2 * math.pi * self.r

    def getArea(self):  # Diện tích
        return math.pi * self.r ** 2

    def isIn(self, a, b):  # Kiểm tra trong đường tròn
        return (a - self.x) ** 2 + (b - self.y) ** 2 <= self.r ** 2


class Square:
    def __init__(self, a):
        self.a = a

    def getPerimeter(self):
        return 4 * self.a

    def getArea(self):
        return self.a ** 2


circle = Circle(0, 0, 5)
print(circle.getPerimeter())  # 31.41592653589793
print(circle.getArea())  # 78.53981633974483
print(circle.isIn(3, 4))  # True
print(circle.isIn(6, 7))  # False

square = Square(5)
print(square.getPerimeter())  # 20
print(square.getArea())  # 25
