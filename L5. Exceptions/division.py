try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError as error:
    print('На ноль делить нельзя!', error)
except (ValueError, TypeError, AttributeError):
    print('Введено не число')
else:
    print('Деление произошло успешно')
finally:
    print('Эта вещь обязательно выведется')
