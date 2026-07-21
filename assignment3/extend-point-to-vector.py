import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def dist(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

class Vector(Point):    
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y) 

point1 = Point(1,1)
point2 = Point(3,2)
point3 = Point(10,20)

print(f"Equality: {point1 == point3}")
print(point1)
print(point1.dist(point2))

vector1 = Vector(1,1)
vector2 = Vector(3,2)
vector3 = Vector(10,20)

print(f"Equality: {vector1 == vector3}")
print(vector1)
vector4 = vector1 + vector3
print(vector4)
