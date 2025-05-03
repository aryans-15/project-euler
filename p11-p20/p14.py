def F(n):
    c = 0
    while n > 1:
        c += 1
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
    return c

a, l = 0, 0
for i in range(1000000):
    L = F(i)
    if L > l:
        l, a = L, i
        
print(a)