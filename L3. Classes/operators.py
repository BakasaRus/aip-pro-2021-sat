class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def __contains__(self, point):
        return self.center.distance(point) <= self.r


class Operator:
    def __init__(self, name):
        self.name = name
        self.towers = []
        self.available = 0

    def __str__(self):
        return f'{self.name} {self.available}'


def input_ints():
    return [int(x) for x in input().split()]


n = int(input())
operators = {}
for i in range(n):
    name = input()
    x, y, r = input_ints()
    tower = Circle(Point(x, y), r)
    if name not in operators:
        operators[name] = Operator(name)
    operators[name].towers.append(tower)

user = Point(*input_ints())

for op in operators.values():
    for tower in op.towers:
        if user in tower:
            op.available += 1

print(len(operators))
for op in operators.values():
    print(op)