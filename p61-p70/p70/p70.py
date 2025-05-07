n, a, r = 10000000, 0, float('inf')
P = list(range(n+1))

for i in range(2, n+1):
    if P[i] == i:
        for j in range(i, n+1, i):
            P[j] -= P[j] // i

for i in range(2, n+1):
    if sorted(str(i)) == sorted(str(P[i])) and i/P[i] < r:
        r, a = i/P[i], i

print(a)
