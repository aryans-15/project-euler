import math

ub, c = 2000000, 0
A, ub2 = [True] * ub, int(ub ** 0.5) + 1

for p in range(2, ub2):
    if A[p]:
        for i in range(p*p, ub, p):
            A[i] = False

for i in range(2, ub):
    if A[i]:
        c += i

print(c)