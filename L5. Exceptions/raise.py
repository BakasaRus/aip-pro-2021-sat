def calc(a, b):
    if a != 1:
        return a * 5 + b

    raise ValueError('Первый аргумент не должен равняться 1')


print(calc(5, 3))
print(calc(1, 8))
