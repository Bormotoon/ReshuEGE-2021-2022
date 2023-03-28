# #demo_2022_perebor
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x == (not y)) <= ((x and w) == z) == 0:
#                     print(x, y, z, w)

# # demo_2023_itertools
from itertools import *


def f(x, y, z, w):
    return (y <= z) and not(w == z) and x

for a in product([0, 1], repeat=4):
    table = [(0, a[0], 0, 1),
             (a[1], 0, a[2], a[3]),
             (1, 0, 0, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
