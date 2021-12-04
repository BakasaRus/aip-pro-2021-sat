import itertools as it

for i in it.repeat(5, 10):
    print(i)

# for i in it.cycle('ABC'):
#     print(i)

for perm in it.permutations('ABC'):
    print(perm)

for i in it.product('ABC', 'XYZ'):
    print(i)
