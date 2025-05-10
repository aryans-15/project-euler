import math

with open('../../files/p99.txt') as f:
    S = [[int(x) for x in line.strip().split(',')] for line in f]

m, l = 0, 0

for i, (b, e) in enumerate(S, start=1):
    v = e * math.log(b)
    if v > m:
        m, l = v, i

print(l)
