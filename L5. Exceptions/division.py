try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError as error:
    print('На ноль делить нельзя!', error)
except ValueError:
    print('Введено не число')
finally:
    print('Эта вещь обязательно выведется')
