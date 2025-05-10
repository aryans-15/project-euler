import itertools

def P(n):
    if n < 2:
        return False
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

def O(p1, p2):
    return P(int(str(p1) + str(p2))) and P(int(str(p2) + str(p1)))

cache = {}
def Oc(p1, p2):
    if (p1, p2) not in cache:
        cache[(p1, p2)] = O(p1, p2)
    return cache[(p1, p2)]

p = [i for i in range(2, 10000) if P(i)]
sz = len(p)

ms = float('inf')
for i in range(sz):
    for j in range(i+1, sz):
        if Oc(p[i], p[j]) and Oc(p[j], p[i]):
            for k in range(j+1, sz):
                if all(Oc(x, p[k]) and Oc(p[k], x) for x in [p[i], p[j]]):
                    for l in range(k+1, sz):
                        if all(Oc(x, p[l]) and Oc(p[l], x) for x in [p[i], p[j], p[k]]):
                            for m in range(l+1, sz):
                                if all(Oc(x, p[m]) and Oc(p[m], x) for x in [p[i], p[j], p[k], p[l]]):
                                    ms = min(ms, sum([p[i], p[j], p[k], p[l], p[m]]))

print(ms)