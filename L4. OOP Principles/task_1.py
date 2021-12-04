class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f'Point<x={self.x}, y={self.y}>'

    def __repr__(self):
        return str(self)


class Vector(Point):
    def length(self):
        return super().dist(Point(0, 0))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

    def __str__(self):
        return f'Vector<x={self.x}, y={self.y}>'


if __name__ == '__main__':
    vector = Vector(5, 0)
    another = Vector(0, 5)
    third = Vector(1, 3)
    print(vector.length())
    print(vector + another)
    print(vector - another)
    print(third * 5)
    print(3 * third)
    print(vector * third)
