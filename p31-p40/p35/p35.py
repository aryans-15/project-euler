ub, c = 1000000, 0
A, s, ub2 = [True] * ub, set(), int(ub ** 0.5) + 1

for p in range(2, ub2):
    if A[p]:
        for i in range(p*p, ub, p):
            A[i] = False

for i in range(2, ub):
    if A[i]: s.add(i)

for x in s:
    tmp, ok = str(x), True
    for i in range(len(tmp)):
        if int(tmp[i:] + tmp[:i]) not in s:
            ok = False
            break
    if ok:
        c += 1

print(c)
    