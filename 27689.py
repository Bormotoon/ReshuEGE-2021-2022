# https://inf-ege.sdamgia.ru/problem?id=27689

'''Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.'''

from math import fmod

s = open('24.txt').read()

count = 0
maxCount = 0

for i in range(len(s)):
    if (s[i] == 'X' and fmod(count, 3) == 0) or \
            (s[i] == 'Y' and fmod(count, 3) == 1) or \
            (s[i] == 'Z' and fmod(count, 3) == 2):
        count += 1

        if count > maxCount:
            maxCount = count
    elif s[i] == 'X':
        count = 1
    else:
        count = 0
    print(maxCount)
