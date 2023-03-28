# #чтение
# with open('24.txt', 'r') as f:
#     #работа с файлом
#
# #запись в файл
# f = open('24.txt', 'w')
# # работа с файлом
# f.close()
#
# #чтение файла в строку
# s = open('24.txt').readline()
# print(s[:20])
#
# #чтение, создание списка, в целочисленный тип
# a = [int(x) for x in open('17.txt')]

# #сочетание КЕ или ЕК
# s = open('24.txt').readline()
# s = s.replace('M', ' ').replace('KK', 'K K').replace('EE', 'E E')
# m = max(s.split(), key=len)
# print(len(m))

#последовательность Е
s = open('24.txt').readline()
s = s.replace('F', ' ').replace('EE', 'E E').replace('DD', 'D D')
m = max(s.split(), key=len)
print(len(m))

