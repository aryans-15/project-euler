def P(n):
    if n < 2:
        return False
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

def T(n):
    s = str(n)
    l = len(s)
    for i in range(1, l):
        if not P(int(s[i:])):
            return False
    for i in range(1, l):
        if not P(int(s[:i])):
            return False
    return True

c, a = 0, 0

for i in range(11, 1000000):
    if P(i) and T(i):
        c += 1
        a += i
    if c == 11:
        print(a)
        quit()