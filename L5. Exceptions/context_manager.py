with open('text.txt', 'w') as file:
    file.writelines(['Hello', 'World'])

try:
    file = open('text.txt', 'w')
    file.write('Hi!')
finally:
    file.close()
