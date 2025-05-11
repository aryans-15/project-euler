import math

lim = 50000000
sq = int(math.isqrt(lim))
A = [True] * (sq+1)
A[0] = A[1] = False
for p in range(2, int(math.isqrt(sq)) + 1):
    if A[p]:
        for m in range(p*p, sq+1, p):
            A[m] = False

A = [i for i, v in enumerate(A) if v]
mp2, mp3, mp4 = int(pow(lim, 1/2)), int(pow(lim, 1/3)), int(pow(lim, 1/4))
P2, P3, P4 = A, [p for p in A if p <= mp3], [p for p in A if p <= mp4]
Q2, Q3, Q4 = [pow(p, 2) for p in P2], [pow(p, 3) for p in P3], [pow(p, 4) for p in P4]
S = [0] * lim

for q4 in Q4:
    for q3 in Q3:
        s43 = q4 + q3
        if s43 >= lim:
            break
        for q2 in Q2:
            s = s43 + q2
            if s >= lim:
                break
            S[s] = 1

print(sum(S))
