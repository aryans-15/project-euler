import math

N, c = 10001, 0
# Dusart's 1999 extension of Rosser's theorem
ub = math.ceil(N * (math.log(N) + math.log(math.log(N)) - 1))
A, ub2 = [True] * ub, int(ub ** 0.5) + 1

for p in range(2, ub2):
    if A[p]:
        for i in range(p*p, ub, p):
            A[i] = False

for i in range(2, ub):
    c += A[i] == True
    if c == N:
        print(i)
        break