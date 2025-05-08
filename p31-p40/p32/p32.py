import itertools

def F(p):
    s = ''.join([str(x) for x in p])
    if int(s[0]) * int(s[1:5]) == int(s[5:]):
        return int(s[5:])
    if int(s[:2]) * int(s[2:5]) == int(s[5:]):
        return int(s[5:])
    return None

s = set()

for p in itertools.permutations([i for i in range(1, 10)]):
    r = F(p)
    if r:
        s.add(r)

print(sum(s))