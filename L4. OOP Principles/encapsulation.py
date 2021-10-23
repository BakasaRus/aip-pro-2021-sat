class Account:
    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def __set_amount(self, amount):
        self.__amount = amount

    def transfer(self, other, to_transfer):
        if self.__amount >= to_transfer:
            self.__amount -= to_transfer
            other.__amount += to_transfer
            return True
        return False


nick = Account(50)
mike = Account(150)

nick.transfer(mike, 50)

print(nick.get_amount(), mike.get_amount())
