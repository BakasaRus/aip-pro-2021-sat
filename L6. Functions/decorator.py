def logging(func):
    def wrapper(*args, **kwargs):
        print('Before calling', func)
        func(*args, **kwargs)
        print('After calling', func)

    return wrapper


@logging
def original(message):
    print(message)


original('Hello!')
original('Python in cool!')
original(message='C# is not')
