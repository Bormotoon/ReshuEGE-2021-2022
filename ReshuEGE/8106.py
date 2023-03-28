# https://inf-ege.sdamgia.ru/problem?id=8106

'''Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наибольшего натурального числа А формула

¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))

тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?'''

A = 10000


def division(m, n):
    return m % n == 0


while True:
    for x in range(1, 1000):
        if not ((not division(x, A)) <= (division(x, 6) <= (not division(x, 4)))):
            break
    else:
        print(A)
        break
    A -= 1
