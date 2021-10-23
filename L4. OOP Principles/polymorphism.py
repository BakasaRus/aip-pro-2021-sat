class Duck:
    def sound(self):
        print('Quack Quack')


class Cat:
    def sound(self):
        print('Meow Meow')


for animal in Duck(), Cat():
    animal.sound()


print(5 + 9)
print('Hello' + 'World')
print([1, 5] + [3, 0])

str(Duck())
str(98)
