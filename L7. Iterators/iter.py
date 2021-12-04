data = [5, 7, 2]

for i in data:
    print(i)

iterator = iter(data)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
