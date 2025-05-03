def S(n):
    a = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a += i
            if n // i != i:
                a += n // i
    return a > n

A, ub, a = set(), 28124, 0

for i in range(1, ub):
    if S(i):
        A.add(i)

for i in range(ub):
    ok = True
    for j in A:
        if j > i:
            break
        if i - j in A:
            ok = False
            break
    if ok:
        a += i

print(a)