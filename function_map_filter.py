l1 = ['1','2','3']
l2 = list(map(int,l1))
def map(func, iter1):
    i = iter(iter1)
    print(func(next(i)))
    print(func(next(i)))
    print(func(next(i)))

print(map1(int, l1)