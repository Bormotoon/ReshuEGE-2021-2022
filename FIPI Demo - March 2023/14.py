# #найти кол-во каких-либо цифр
x = 8*729**1121+7*81**1122+6*9**1123-2023
count = 0
while x:
    if x % 9 == 8:
        count += 1
    x //= 9
print(count)
# # #найти цифры или основание СС в выражении для люб
# # k = 0
# # for x in range(64, 15*16+5):
# #     h = hex(x)[2:]
# #     o = oct(x)[2:]
# #     if h[-1] == '5' and o[-2] == '0' and len(h) == 2 and len(o) == 3:
# #         k += 1
# # print(k)
# # # # через строки осн 2-36
'''alf = '0123456789abcde'
for x in alf:
    s = int('123'+x+'5', 15) + int('1'+x+'233', 15)
        if s % 14 == 0:
            print(s//14)
# # #'''
# #Статград
# for p in range(10, 37):
#     for x in range(1, p):
#         for y in range(1, p):
#             a = 3*p**3+2*p**2+x*p+8
#             b = x*p**3+x*p**2+x*p+9
#             c = y*p**3+y*p**2+0*p+2
#             if a + b == c:
#                 print(y*p**2+y*p+x)
