from collections import deque

with open('../../files/p79.txt') as f:
    S = [[x for x in line.strip()] for line in f if line.strip()]

g, deg = {}, {}
for e in S:
    for c in e:
        if c not in deg:
            deg[c] = 0
        if c not in g:
            g[c] = set()

for e in S:
    for i in range(2):
        if e[i+1] not in g[e[i]]:
            g[e[i]].add(e[i+1])
            deg[e[i+1]] += 1

q, s = deque([n for n in deg if deg[n] == 0]), []

while q:
    n = q.popleft()
    s.append(n)
    for u in g[n]:
        deg[u] -= 1
        if deg[u] == 0:
            q.append(u)

print(''.join(s))