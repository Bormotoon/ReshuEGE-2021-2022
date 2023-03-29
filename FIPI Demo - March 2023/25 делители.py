# #алгоритм простой
# x = 1_000_000_000
# d = []
# for i in range(1, x + 1):
#     if x % i == 0:
#         d.append(i)
# print(d)
#


#усовершенствованный алгоритм
def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
print(div(1_000_000_000_000))

# #2926
# def div(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
#
# for i in range(209834, 209857 + 1):
#     if len(div(i)) == 4:
#         print(i, div(i)[-2], div(i)[-1])

#2859
# def div(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
#
# for i in range(81234, 134689 + 1):
#     if len(div(i)) == 5:
#         print(div(i)[1], div(i)[-2])

# # 5766
# def div(x):
#     d = set()
#     for i in range(1, int(x ** 0.25) + 1):
#         if x % i == 0:
#             d.add(i)
#             d.add(i ** 2)
#             d.add(x // i)
#             d.add((x // i) ** 2)
#     return sorted(d)


# for i in range(10 ** 9, 5 * 10 ** 9 + 1):
#     if len(div(i)) == 9:
#         print(i, div(i)[-2])
