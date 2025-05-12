import math

lim, DS, C = 1000000, {}, []
used = [False] * (lim + 1)

def D(n):
    A = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            A.append(i)
            if i != n // i:
                A.append(n // i)
    return A

def trim(chain):
    return chain[chain.index(DS[chain[-1]]):]

for n in range(1, lim):
    DS[n] = sum(D(n))

for i in range(1, lim):
    n = i
    cur = []
    while True:
        if n > lim or used[n]:
            break
        cur.append(n)
        used[n] = True
        n = DS.get(n, 0)
        if n in cur:
            C.append(trim(cur))
            break

c, sz = C[0], len(C[0])
for x in C:
    if len(x) > sz:
        sz, c = len(x), x

print(min(c))
