# #prostoe
# s = '2' * 122
# while '2222' in s or '888' in s:
#     if '2222' in s:
#         s = s.replace('2222', '8', 1)
#     else:
#         s = s.replace('888', '2', 1)
# print(s, s.count('2') * 2 + s.count('8') * 8)

# #Polyakov_2092
# s = '>' + '1' * 25 + '2' * 17 + '3' * 10
# while '>1' in s or '>2' in s or '>3' in s:
#     s = s.replace('>1', '22>3', 1)
#     s = s.replace('>2', '2>', 1)
#     s = s.replace('>3', '11>2', 1)
#print(1 * s.count('1') + 2 * s.count('2') + 3 * s.count('3'))





# #2_найти исходную строку (a-"1", b-"2", c-"3")
# for a in range(46):
#     for b in range(46):
#       for c in range(46):
# # зададим исходную строку
#          s = '0' + a*'1' + b*'2' + c*'3'
# # запустим цикл перебора и замены
#          while ('01' in s) or ('02' in s) or ('03' in s):
#             s = s.replace('01', '30', 1)
#             s = s.replace('02', '3103', 1)
#             s = s.replace('03', '1201', 1)
# # выведем результат, удовлетворяющий условию задачи (с - количество "3" в исходной строке)
#          if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
#              print(a, b, c)

#
# for x in range(1,10000):
#     s = '0'+'1'*x+'2'*x+'0'
#     while not '00' in s:
#         if '011' in s:
#             s = s.replace('011','101',1)
#         else:
#             s = s.replace('01','40',1)
#             s = s.replace('02','20',1)
#             s = s.replace('0222', '1401', 1)
#         n1 = s.count('1')
#         n2 = s.count('2')
#         n4 = s.count('4')
#         if n1 == 6 and n2 == 9:
#             print(n4)

# #statgrad
# def div(x):
#     d = set()
#     for i in range(1, int(x**0.5)+1):
#         if x % i == 0:
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
#
#
# for m in range(1000):
#     s = '>' + '1' * 15 + '2' * 35 + '3' * m
#     while '>1' in s or '>2' in s or '>3' in s:
#         s = s.replace('>1', '2>', 1)
#         s = s.replace('>2', '3>', 1)
#         s = s.replace('>3', '11>', 1)
#     s = s[:-1]
#     s1 = sum(list(map(int, s)))
#     if len(div(int(s1))) == 5:
#         print(m)

# #статград_2023
# a = []
# for k1 in range(50):
#     for k2 in range(50):
#         for k3 in range(50):
#             for k4 in range(50):
#                 if 2*k1 + k3 == 2*k2 + k4 and k2 + 2*k4 == 40 and k1 + 2*k3 > 50:
#                     a.append(k1 + 2*k3)
# print(min(a))