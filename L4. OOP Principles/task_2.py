from task_1 import Point, Vector


class Vehicle:
    def __init__(self, start):
        self.position = start
        self.direction = Vector(0, 0)
        self.is_recording = False
        self.path = [start]

    def move(self, n):
        for i in range(n):
            self.position = Point(self.position.x + self.direction.x, self.position.y + self.direction.y)
            if self.is_recording:
                self.path.append(self.position)


class Car(Vehicle):
    def __init__(self, start, gas, gas_per_unit):
        super().__init__(start)
        self.gas = gas
        self.__gas_per_unit = gas_per_unit

    def __gas_usage(self):
        return self.direction.length() * self.__gas_per_unit

    def move(self, n):
        for i in range(n):
            if self.__gas_usage() <= self.gas:
                self.position = Point(self.position.x + self.direction.x, self.position.y + self.direction.y)
                self.gas -= self.__gas_usage()
                if self.is_recording:
                    self.path.append(self.position)
            else:
                break


bicycle = Vehicle(Point(0, 0))
bicycle.direction = Vector(1, 0)
bicycle.is_recording = True
bicycle.move(5)
print(bicycle.path)

car = Car(Point(0, 0), 10, 0.5)
car.direction = Vector(1, 1)
car.is_recording = True
car.move(5)
print(car.path)
print(car.gas)
car.move(15)
print(car.path)
print(car.gas)
