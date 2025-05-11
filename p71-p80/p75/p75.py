import math

lim = 1500000
A = [0] * (lim + 1)

for m in range(2, int((lim // 2)**0.5) + 1):
    for n in range(1+m%2, m, 2):
        if math.gcd(m, n) != 1:
            continue

        p = 2 * m * (m + n)
        if p > lim:
            break

        k = 1
        while k * p <= lim:
            A[k * p] += 1
            k += 1

print(sum([1 for x in A if x == 1]))
