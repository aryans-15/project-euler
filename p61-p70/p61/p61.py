def P(s, n):
    if s == 3:
        return n * (n + 1) // 2
    elif s == 4:
        return n*n
    elif s == 5:
        return n * (3*n - 1) // 2
    elif s == 6:
        return n * (2*n - 1)
    elif s == 7:
        return n * (5*n - 3) // 2
    return n * (3*n - 2)
    
def ok(a, b):
    return str(a)[2:] == str(b)[:2]

def R(P, used, A):
    if len(P) == 6:
        if ok(P[-1][1], P[0][1]):
            return [x[1] for x in P]
        return None
    ls = str(P[-1][1])[2:]
    for s in A:
        if s in used:
            continue
        for num in A[s]:
            if str(num)[:2] == ls:
                res = R(P + [(s, num)], used | {s}, A)
                if res:
                    return res
    return None

A, lb, ub = {s: [] for s in range(3, 9)}, 1000, 10000
for s in range(3, 9):
    n = 1
    while True:
        p = P(s, n)
        if p >= ub:
            break
        if p >= lb:
            A[s].append(p)
        n += 1

for s in A:
    for n in A[s]:
        result = R([(s, n)], {s}, A)
        if result:
            print(sum(result))
            quit()
