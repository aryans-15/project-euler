import itertools

A, t = set(range(1, 11)), ""

for oc in itertools.combinations(A, 5):
    oc = list(oc)
    for O in itertools.permutations(oc):
        if O[0] != min(O):
            continue
        ic = A - set(O)
        for I in itertools.permutations(ic):
            ok = True
            for i in range(1, 5):
                s = O[i] + I[i] + I[(i+1) % 5]
                if s != O[0] + I[0] + I[1]:
                    ok = False
                    break
            if not ok:
                continue
            s = ""
            for i in range(5):
                s += str(O[i]) + str(I[i]) + str(I[(i+1) % 5])
            if len(s) == 16 and s > t:
                t = s

print(t)
