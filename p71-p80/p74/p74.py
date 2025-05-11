import math

A, c = [math.factorial(i) for i in range(10)], 0

def C(n, d):
    if n in d:
        return 0
    d.add(n)
    return C(sum(A[int(d)] for d in str(n)), d) + 1

for i in range(1000001):
    c += C(i, set()) == 60

print(c)

