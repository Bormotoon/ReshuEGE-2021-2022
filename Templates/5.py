#standart

n = 33
n2 = bin(n)[2:]
if n2.count('1') % 2 == 0:
    n2 = '1' + n2[2:] + '0'
else:
    n2 = '11' + n2[2:] + '1'
print(n, int(n2, 2))