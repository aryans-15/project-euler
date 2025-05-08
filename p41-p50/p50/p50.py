l, ml, mp = 1000000, 0, 0
P, p = [True] * (l + 1), 2

while p*p <= l:
    if P[p]:
        for i in range(p*p, l+1, p):
            P[i] = False
    p += 1

P2 = [p for p in range(2, l) if P[p]]
ps, psl = set(P2), len(P2)

for i in range(psl):
    for j in range(i+ml, psl):
        sm = sum(P2[i:j])
        if sm < l:
            if sm in ps and j - i > ml:
                ml, mp = j - i, sm
        else:
            break

print(mp)
