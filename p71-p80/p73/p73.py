import math

lim, c = 12000, 0
for d in range(2, lim+1):
    ns, ne = d//3 + 1, (d - 1)//2
    for n in range(ns, ne+1):
        c += math.gcd(n, d) == 1

print(c)