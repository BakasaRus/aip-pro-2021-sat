from typing import Any


class Repeater:
    __value: Any

    def __init__(self, value: Any):
        self.__value = value

    def __iter__(self) -> 'Repeater':
        return self

    def __next__(self) -> Any:
        return self.__value


for i in Repeater(5):
    print(i)
