import math

a, b = 1, 1

for n in range(10, 100):
    for d in range(n+1, 100):
        ns, ds = str(n), str(d)
        if '0' in ns and '0' in ds:
            continue
        cd = set(ns) & set(ds)
        for dig in cd:
            if dig == '0':
                continue
            nns, nds = ns.replace(dig, '', 1), ds.replace(dig, '', 1)
            if nns == '' or nds == '':
                continue
            nn, nd = int(nns), int(nds)
            if nd == 0:
                continue
            if n * nd == d * nn:
                a, b = a * n, b * d
        
print(b // math.gcd(a, b))