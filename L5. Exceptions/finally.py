def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        return 0


print(div(5, 2))
print(div(5, 0))
