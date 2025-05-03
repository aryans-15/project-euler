import math

A, t, a = list(range(10)), 999999, []

for i in range(9, -1, -1):
    f = math.factorial(i)
    a.append(A.pop(t // f))
    t %= f

print(''.join(map(str, a)))
