import math

def F(c):
    a = 0
    for s in range(2, 2*c + 1):
        if math.isqrt(c*c + s*s)**2 == c*c + s*s:
            a += (s // 2) - max(0, s - c - 1)
    return a

t, c = 0, 0
while t <= 1000000:
    c += 1
    t += F(c)
print(c)