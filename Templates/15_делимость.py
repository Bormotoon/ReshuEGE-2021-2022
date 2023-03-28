def f(x, a):
    return (x & 48 == 0) or (x & 28 != 0) or (x & a != 0)


for a in range(0, 1000):
    if all(f(x, a) == 1 for x in range(0, 1000)):
        print(a)