from math import gcd

lim, bn, bd = 1000000, 0, 1

for d in range(2, lim+1):
    n = (3*d - 1) // 7
    if gcd(n, d) == 1:
        if n * bd > bn * d: 
            bn, bd = n, d

print(bn)