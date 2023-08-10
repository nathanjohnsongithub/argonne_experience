import itertools

arr = itertools.takewhile(lambda x: x == 5, [1,5,3,4,5,6,7,8])

for n in arr:
    print(n)
