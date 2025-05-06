S, i, A, j = "", 1, 1, 1
while len(S) < 1e6:
    S += str(i)
    i += 1
while j <= 1e6:
    A *= int(S[j - 1])
    j *= 10
print(A)