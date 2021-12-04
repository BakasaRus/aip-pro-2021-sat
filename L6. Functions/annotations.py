from typing import List, Dict, Union, Optional

Number = Union[int, float]


def fun(x: Number, y: Number) -> Number:
    # return 'Test'
    return x + y


a: int = 59
print(a)
a = 'Test'
print(a)

data: List[int] = [int(x) for x in input().split()]
phones: dict[int, str] = {1112223: 'Иванов В.П.'}

print(fun(5, 9))
print(fun(5, 9.0))
print(fun(5.0, 9.0))
print(fun(5.0, 9))

x: Optional[int] = 5
x = None
x = 'xdghdfg'
