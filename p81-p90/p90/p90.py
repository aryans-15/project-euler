import itertools

S = [(int(a), int(b)) for a, b in map(lambda x: f"{x:02}", [1, 4, 9, 16, 25, 36, 49, 64, 81])]

def F(D):
    D = set(D)
    if 6 not in D and 9 not in D:
        return D
    return D | {6, 9}

def O(cube1, cube2):
    A, B = F(cube1), F(cube2)
    for a, b in S:
        if not ((a in A and b in B) or (a in B and b in A)):
            return False
    return True

d = list(range(10))
c, a = list(itertools.combinations(d, 6)), 0
n = len(c)

for i in range(n):
    for j in range(i, n):
        a += O(c[i], c[j])

print(a)
