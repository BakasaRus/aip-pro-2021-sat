class Driver:
    def __init__(self, name, laps):
        self.name = name
        self.laps = laps
        self.total = sum(laps)

    def __lt__(self, other):
        return isinstance(other, Driver) and self.total < other.total


n, m = [int(x) for x in input().split()]
drivers = []
for i in range(n):
    name = input()
    laps = [int(x) for x in input().split()]
    drivers.append(Driver(name, laps))

print(min(drivers).name)
