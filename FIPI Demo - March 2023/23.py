def f(c, e):
    if c > e or c == 22: return 0
    if c == e: return 1
    if c < e: return f(c + 1, e) + f(c * 2, e)
print(f(2, 7) * f(7, 49))
    
