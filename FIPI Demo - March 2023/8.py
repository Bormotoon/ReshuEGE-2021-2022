# s = 'авеикнор'
# k = 0
# for a in s:
#     for b in s:
#         for c in s:
#             sl = a + b + c
#             if sl.count('в') == 1:
#                 k += 1
#                 if sl.count('а') == 0:
#                     print(k)

# #досрок_2022_БАТЫР
# from itertools import *
# for s in product('абрты', repeat=5):
#     s1 = "".join(map(str, s))
#     if not ('ы' in s1) and not ('аа' in s1) and not ('ааа' in s1) and not ('аааа' in s1) and not ('ааааа' in s1):
#         print(s1)

# #
# answer = 0
# not_use = ['16', '61', '36', '63', '56', '65', '76', '67']
#
# for i1 in '1234567':
#     for i2 in '01234567':
#         for i3 in '01234567':
#             for i4 in '01234567':
#                 for i5 in '01234567':
#
#                     numb = i1 + i2 + i3 + i4 + i5
#
#                     if numb.count('6') == 1 and sum([int(x in numb) for x in not_use]) == 0:
#                         answer += 1
#
# print(answer)

# z = ['16', '36', '56', '76', '61', '63', '65', '67']
# m = 0
# s = '01234567'
# for a in '1234567':
#     for b in s:
#         for c in s:
#             for d in s:
#                 for e in s:
#                     sl = a + b + c + d + e
#                     k = 0
#                     for i in range(len(z)):
#                         if z[i] in sl:
#                             k += 1
#                     if k == 0 and sl.count('6') == 1:
#                         m += 1
# print(m)

# #5128_Polyakov
# alf = '0123456789abcdef'
# k = 0
# for a in '23456789abcdef':
#     for b in alf:
#         for c in alf:
#             for d in alf:
#                 s = a + b + c + d + 'a' + 'b'
#                 print(s)
#                 k += 1
# print(k)

s = 'азкмуы'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        sl = a + b + c + d + e + f
                        k += 1
                        if sl[0] != 'ы' and sl.count('м') == 2 and sl.count('ы') <= 1:
                            print(sl, k)










