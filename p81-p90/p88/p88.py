import math
import sys

km, lim = 12000, 24000
B = [lim+1] * (km + 1)

def dfs(start_fac, prod, sm, count):
    k = prod - sm + count
    if 2 <= k <= km:
        B[k] = min(B[k], prod)
    for f in range(start_fac, lim // prod + 1):
        new_prod = prod * f
        if new_prod > lim:
            break
        dfs(f, new_prod, sm + f, count + 1)

dfs(2, 1, 0, 0)
print(sum(set(B[2:])))
