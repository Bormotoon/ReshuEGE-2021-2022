 def f(x, a1, a2):
    return ((a1 <= x <= a2) <= (430 <= x <= 490)) or (440 <= x <= 530)

m = 0
for a1 in range(400, 600):
    for a2 in range(a1 + 1, 600):
        if all(f(x, a1, a2) == 1 for x in range(400, 600)):
            m = max(a2 - a1, m)
print(m/10)

# def f(x,y,a):
#     return ((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9))
#
# for a in range(500):
#     flag = 0
#     for x in range(1000):
#         for y in range(1000):
#             if not(f(x,y,a)):
#                 flag = 1
#                 break
#         if flag:
#             break
#     else:
#         print(a)


