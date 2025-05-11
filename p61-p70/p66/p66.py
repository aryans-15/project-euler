import math

def F(D):
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        return None
    m, d, a = 0, 1, a0
    hp, h, kp, k = 1, a, 0, 1
    while h*h - D*k*k != 1:
        m = d*a - m
        d = (D - m*m) // d
        a = (a0 + m) // d
        hp, h, kp, k = h, a*h + hp, k, a*k + kp
    return h

bx, bd = 0, 0

for i in range(2, 1001):
    s = F(i)
    if s is None:
        continue
    if s > bx:
        bx, bd = s, i

print(bd)
