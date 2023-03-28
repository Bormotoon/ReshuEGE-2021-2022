# https://inf-ege.sdamgia.ru/problem?id=23916

'''Для какого наименьшего целого неотрицательного числа А выражение

(x + 2y < A) ∨ (y > x) ∨ (x > 20)

тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?'''

A = 1

while True:
    for x in range(0, 100):
        for y in range(0, 100):
            if not ((x + 2 * y < A) or (y > x) or (x > 20)):
                break
        else:
            continue
        break
    else:
        print(A)
        break
    A += 1
