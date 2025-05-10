a, mn = 0, float('inf')

for m in range(1000):
    for n in range(1000):
        p = m * n * (m + 1) * (n + 1) // 4
        if abs(2000000 - p) < mn:
            mn = abs(2000000 - p)
            a = m * n

print(a)