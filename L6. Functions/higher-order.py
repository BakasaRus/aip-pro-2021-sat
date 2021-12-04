from typing import Callable, Any


def sound(being: str) -> Callable[[], str]:
    def meow():
        return 'Meow!'

    def default():
        return 'Default!'

    if being == 'cat':
        return meow
    else:
        return default


def fun(a: int, b: int) -> int:
    return a + b


def greet() -> str:
    return 'Hello!'


def logging(function: Callable) -> Any:
    print('Calling function', function)
    return function()


another = fun

print(fun(5, 3))
del fun
print(another(5, 3))

cat = sound('cat')
person = sound('person')

print(cat(), person())
print(logging(greet))
