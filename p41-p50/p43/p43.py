import itertools

A, c = [2, 3, 5, 7, 11, 13, 17], 0

P = list(itertools.permutations([i for i in range(10)]))
for p in P:
    v, ok = ''.join(map(str, p)), True
    for i in range(7):
        if int(v[i+1:i+4]) % A[i]:
            ok = False
            break
    if ok:
        c += int(v)

print(c)