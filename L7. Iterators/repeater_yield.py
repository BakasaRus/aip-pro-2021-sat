from typing import Any, Generator


def repeater(x: Any) -> Generator:
    while True:
        yield x


repeat = repeater(5)
print(next(repeat))
print(next(repeat))
print(next(repeat))


for i in repeater(5):
    print(i)
