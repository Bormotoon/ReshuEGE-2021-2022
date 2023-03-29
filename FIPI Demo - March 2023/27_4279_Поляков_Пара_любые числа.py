f = open('27-73a.txt')
n = int(f.readline())
a = [int(x) for x in f]
maxs = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s % 93 == 0 and s % 2 != 0 and s > maxs:
            maxs = s
print(maxs)

# f = open('27-73b.txt')
# n = int(f.readline())
# maxs = 0
# s = 0
# mini = [10**20]*93
# for i in range(n):
#     x = int(f.readline())
#     s += x
#     if s % 93 == 0 and s % 2 != 0: maxs = max(maxs, s)
#     s1 = s - mini[s % 93 and not s % 2]
#     maxs = max(maxs, s1)
#     mini[s % 93 and not s % 2] = min(mini[s % 93 and not s % 2], s)
# print(maxs)