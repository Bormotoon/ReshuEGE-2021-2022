# https://inf-ege.sdamgia.ru/problem?id=27693

'''Текстовый файл состоит не более чем из 106 символов A, B и C. Определите максимальное количество идущих подряд символов C.

Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.'''

file = open("24.txt")
the_text = list(file)
count, cunt_max = 1, 1
for i in range(1, len(the_text)):
    if the_text[i] == the_text[i - 1] and the_text[i] == "C":
        count += 1
        if count > cunt_max:
            cunt_max = count
print(cunt_max)
