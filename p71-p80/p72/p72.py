lim = 1000000
P = list(range(lim+1))

for i in range(2, lim+1):
    if P[i] == i:
        for j in range(i, lim+1, i):
            P[j] -= P[j] // i

print(sum(P))