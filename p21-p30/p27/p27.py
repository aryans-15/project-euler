def P(n):
    if n < 0:
        return False
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

C, p = 0, 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        c, n = 0, 0
        while P(n*n + a*n + b):
            c, n = c + 1, n + 1
        if c > C:
            C = c
            p = a * b

print(p)
