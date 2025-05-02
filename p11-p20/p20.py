import math

S, a = str(math.factorial(100)), 0

for d in S:
    a += int(d)

print(a)