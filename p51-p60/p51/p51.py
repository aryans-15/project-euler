import math
import itertools

lim = 1000000
A = [True] * (lim+1)
A[0] = A[1] = False
for p in range(2, int(math.isqrt(lim))+1):
    if A[p]:
        for m in range(p*p, lim+1, p):
            A[m] = False

P = [i for i, v in enumerate(A) if v]

def F(s, pos, d):
    t = list(s)
    for i in pos:
        t[i] = d
    return ''.join(t)

for p in P:
    s = str(p)
    l = len(s)
    for r in range(1, l):
        for pos in itertools.combinations(range(l), r):
            digits = {s[i] for i in pos}
            if len(digits) != 1:
                continue
            fam = []
            for d in '0123456789':
                if pos[0] == 0 and d == '0':
                    continue
                replaced = F(s, pos, d)
                num = int(replaced)
                if num < lim and A[num]:
                    fam.append(num)
            if len(fam) >= 8:
                print(min(fam))
                quit()
