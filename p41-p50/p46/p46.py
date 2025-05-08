import math

def P(n):
    if n < 2:
        return False
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

def F(n):
    for p in range(2, n):
        if P(p):
            rem = n - p
            if rem % 2 == 0:
                k_squared = rem // 2
                k = int(math.isqrt(k_squared))
                if k * k == k_squared:
                    return True
    return False

n = 9
while True:
    if not P(n) and not F(n):
        print(n)
        quit()
    n += 2
