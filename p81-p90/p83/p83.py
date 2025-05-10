import heapq

with open('../../files/p83.txt') as f:
    S = [[int(x) for x in line.strip().split(",")] for line in f if line.strip()]

N = len(S)
D = [[float('inf')] * N for _ in range(N)]
D[0][0] = S[0][0]
pq = [(S[0][0], 0, 0)]

while pq:
    cost, i, j = heapq.heappop(pq)
    if cost > D[i][j]:
        continue
    for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
        if not (0 <= x < N and 0 <= y < N):
            continue
        nc = cost + S[x][y]
        if nc < D[x][y]:
            D[x][y] = nc
            heapq.heappush(pq, (nc, x, y))

print(D[-1][-1])