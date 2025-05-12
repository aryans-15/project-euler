import math

with open('../../files/p98.txt') as f:
    S = f.read().replace('"', '').split(",")

def W(word):
    mp, P, nxt = {}, [], 0
    for ch in word:
        if ch not in mp:
            mp[ch] = nxt
            nxt += 1
        P.append(mp[ch])
    return tuple(P)

def G(ml):
    sq, n = {}, 1
    while True:
        s = str(n * n)
        if len(s) > ml:
            break
        sq.setdefault(len(s), []).append(s)
        n += 1
    return sq

A, sq_pat, best = {}, {}, 0

for w in S:
    key = ''.join(sorted(w))
    A.setdefault(key, []).append(w)

grps = [grp for grp in A.values() if len(grp) > 1]
sq_len = G(max(len(w) for w in S))

for L, sql in sq_len.items():
    sq_pat[L] = {}
    for sq in sql:
        pat = W(sq)
        sq_pat[L].setdefault(pat, []).append(sq)

for group in grps:
    L, wp = len(group[0]), W(group[0])
    for sq in sq_pat.get(L, {}).get(wp, []):
        mp = {ch: d for ch, d in zip(group[0], sq)}
        if mp[group[0][0]] == '0':
            continue
        sq1 = int(math.isqrt(int(sq)))
        if sq1 * sq1 != int(sq):
            continue
        for other in group[1:]:
            if mp.get(other[0], '0') == '0':
                continue
            try:
                res = ''.join(mp[ch] for ch in other)
            except KeyError:
                continue
            val = int(res)
            if math.isqrt(val)**2 == val:
                best = max(best, int(sq), val)

print(best)
