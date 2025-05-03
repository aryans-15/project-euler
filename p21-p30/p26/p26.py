import math

A, ml = 0, 0

for d in range(2, 1000):
    if math.gcd(d, 10) != 1:
        continue
    rem, seen, pos = 1, {}, 0
    while rem != 0 and rem not in seen:
        seen[rem] = pos
        rem = (rem * 10) % d
        pos += 1
    if rem in seen:
        cyc = pos - seen[rem]
        if cyc > ml:
            ml = cyc
            A = d

print(A)