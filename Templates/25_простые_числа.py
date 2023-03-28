#standart_function
#x>1 (1 - не простое число)
#х не делится ни на одно число из [2; x**0.5]
def p(x):
    return not (not (x > 1) or not all(x % i for i in range(2, int(x ** 0.5) + 1)))


#2897
k = 0
for x in range(2358827, 2358891 + 1):
    if p(x):
        k += 1
        print(k, x)