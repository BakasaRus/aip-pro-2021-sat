class Person:
    def __init__(self, name, age):
        print('Hi from Person')
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hi, my name is {self.name}')


class Student(Person):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

    def greet(self):
        print(f'Hi, my name is {self.name} from {self.group}')

    def survive(self):
        print(f'{self.name} is lucky')


person = Person('Иван Петров', 38)
student = Student('Вася Пупкин', 19, 'M3212')

person.greet()
student.greet()

student.survive()
print(student.group)
