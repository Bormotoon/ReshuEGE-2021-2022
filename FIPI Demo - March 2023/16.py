#standart
def f(n):
    if n < 3: return 1
    if n > 2 and n % 2 == 0: return f(n - 1) + n - 1
    if n > 2 and n % 2 != 0: return f(n - 2) + 2 * n


print(f(32) - f(30))

# #2 function_226
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - 2 * g(n - 1)
#
#
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + 2 * g(n - 1)
#
#
# print(g(21))

# #otbor_2278
# def f(n):
#     if n > 25: return 2 * n * n * n + 1
#     if n <= 25: return f(n + 2) + 2 * f(n + 3)
#
#
# c = 0
# for n in range(1, 1001):
#     if f(n) % 11 == 0:
#         c += 1
# print(c)

# #bol'shaya_glubina_6102
# def f(n):
#     if n < 10: return n
#     if 10 <= n < 1000: return f(n//10) + f(n%10)
#     if n >= 1000: return f(n // 1000) - f(n % 1000)
#
#
# c = 0
# for n in range(10**6):
#     if f(n) == 0:
#         c += 1
# print(c)

# #*_238
# def f(n):
#   if n > 0: return g(n - 1)
# def g(n):
#     c = 0
#     c += 1
#     if n > 1:
#         c += 1
#         c += f(n - 2)
#     return c
# print(f(13))

# #dano F(n)
# def f(n):
#     if n < 2: return 1
#     if n >= 2 and n % 3 == 0: return f(n/3) - 1
#     if n >= 2 and n % 3 != 0: return f(n - 1) + 17
# c = 0
# for n in range(1, 10**5 + 1):
#     if f(n) == 43:
#         c += 1
# print(c)

# #NEstandart
# from sys import *
# setrecursionlimit(10000)
#
# def f(n):
#     if n <= 2: return 1
#     if n > 2: return n * f(n - 2)
# #
# #
# print(f(5000) / (f(4994)))
# #
#есть вызов f(n+2) невозможно
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n <= 1: return 1
#     if n > 1 and n % 2 == 0: return 3 + f(n/2 - 1)
# n = 2
# while n < 1000:
#     try:
#         r = f(n)
#         if r == 19:
#             print(n)
#             break
#     except:
#         pass
#     n += 1
#




















