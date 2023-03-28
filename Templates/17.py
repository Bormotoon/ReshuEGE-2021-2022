a = [int(x) for x in open('17.txt')]
ans = []
a8 = 0
for j in range(len(a)):
    if a[j] % 10 == 8:
        a8 = max(a8, a[j])

for i in range(len(a) - 1):
    if ((a[i] % 10 == 8 and a[i+1] % 10 != 8) or (a[i] % 10 != 8 and a[i+1] % 10 == 8)) and (((a[i] - a[i+1])**2) < (a8**2)):
        ans.append((a[i] - a[i+1])**2)
print(len(ans), min(ans)
