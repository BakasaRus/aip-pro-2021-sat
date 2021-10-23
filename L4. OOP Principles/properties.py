class Account:
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        print('Hello from getter')
        return self.__amount

    @amount.setter
    def amount(self, amount):
        print('Hello from setter')
        self.__amount = amount


nick = Account(50)
mike = Account(150)

nick.amount -= 50
mike.amount += 50

print(nick.amount, mike.amount)
