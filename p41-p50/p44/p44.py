def P(n):
    return n * (3*n - 1) // 2

lim, md = 3000, float('inf')
A = [P(n) for n in range(1, lim+1)]
S = set(A)

for j in range(lim):
    for i in range(j):
        s, d = A[j]+A[i], A[j]-A[i]
        if s in S and d in S:
            md = min(md, d)
    if md is not None and A[j] - A[j-1] > md:
        break

print(md)
