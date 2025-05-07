import itertools

def P(n):
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

a = 0

for i in range(9, 0, -1):
    A = list(itertools.permutations([j for j in range(1, i+1)]))
    for p in A:
        v = int(''.join(map(str, p)))
        if P(v):
            a = max(a, v)
    if a > 0:
        print(a)
        break