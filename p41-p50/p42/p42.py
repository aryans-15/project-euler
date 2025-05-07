import math

with open('../../files/p42.txt') as f:
    S = f.read().replace('"', '').split(",")

a = 0

for w in S:
    v = sum(ord(c) - ord('A') + 1 for c in w)
    d = 1 + 8 * v
    if pow(math.isqrt(d), 2) == d:
        a += 1

print(a)