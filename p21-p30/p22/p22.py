with open('../files/p22.txt') as f:
    S = sorted(f.read().replace('"', '').split(","))

N, a = len(S), 0
for i in range(N):
    C = 0
    for c in S[i]:
        C += ord(c) - ord('A') + 1
    a += (i + 1) * C

print(a)