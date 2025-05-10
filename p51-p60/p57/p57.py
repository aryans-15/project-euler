c, n, d = 0, 3, 2

for i in range(1, 1000):
    n, d = n+2*d, n+d
    c += len(str(n)) > len(str(d))

print(c)