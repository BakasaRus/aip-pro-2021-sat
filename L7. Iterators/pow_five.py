class PowFive:
    __max_pow: int
    __cur_pow: int

    def __init__(self, max_pow: int) -> None:
        self.__max_pow = max_pow
        self.__cur_pow = 0

    def __iter__(self):
        self.__cur_pow = 0
        return self

    def __next__(self):
        self.__cur_pow += 1
        if self.__cur_pow > self.__max_pow:
            raise StopIteration
        return 5 ** self.__cur_pow


pow_five = PowFive(15)

print('First')
for power in pow_five:
    print(power)

# pow_five_2 = PowFive(15)

print('Second')
for power in pow_five:
    print(power)
