# #flag
# for a in range(0, 500):
#     flag = 0
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (((x + y) <= 22) or (y <= (x - 6)) or (y >= a)) == 0:
#                 flag = 1
#                 break
#     if flag == 0:
#         print(a)


# def f(x, a):
#     return (x*x + y*y < a) or (x>3) or (y >= 5)
#
#
# ans = []
# for a in range(0, 500):
#     for x in range(1000):
#         for y in range(1000):
#             if not f(x, a):
#                 break
#             else:
#                 ans.append(a)
# print(ans)

def f(x, y, a):
    return (x * x + y * y < a) or (x > 3) or (y >= 5)


for a in range(0, 1000):
    if all(f(x, y, a) == 1 for x in range(0, 100) for y in range(0, 100)):
        print(a)