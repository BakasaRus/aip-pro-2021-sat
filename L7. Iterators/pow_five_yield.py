from typing import Generator


def pow_five(max_pow: int) -> Generator:
    cur_pow: int = 0
    while cur_pow <= max_pow:
        yield 5 ** cur_pow
        cur_pow += 1


def pow_tabulate(max_number: int) -> Generator:
    def pow_x(max_pow: int) -> Generator:
        cur_pow: int = 0
        while cur_pow <= max_pow:
            if cur_number ** cur_pow >= 200:
                return
            yield cur_number ** cur_pow
            cur_pow += 1

    cur_number: int = 1
    while cur_number <= max_number:
        yield pow_x
        cur_number += 1


gen = pow_five(15)

print('First')
for x in gen:
    print(x)

print('Second')
for x in gen:
    print(x)

for gen in pow_tabulate(10):
    for x in gen(5):
        print(x)
