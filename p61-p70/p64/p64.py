import math

def P(n):
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return 0
    m, d, a, p = 0, 1, a0, 0
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        p += 1
        if a == 2 * a0:
            break
    return p

c = 0

for i in range(10001):
    c += P(i) % 2

print(c)