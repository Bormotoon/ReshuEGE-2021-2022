#циклические_пути_ДЕМО_2023
s = 'АБГ БД ВАБГД ГЕЖ ДЕИЛ ЕЛВ ЖЕ ИЛ КЖ ЛЖК'
d = {c[0]:c[1:] for c in s.split()}


def f(s, e):
    if len(s) > 1 and s[-1] == e: return 1
    return sum(f(s + c, e) for c in d[s[-1]])


print(f('Е', 'Е'))
