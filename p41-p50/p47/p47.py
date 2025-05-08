def D(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d)
            n //= d
        d += 1
    if n > 1:
        f.add(n)
    return len(f)

for i in range(1000000):
    if D(i) == 4 and D(i+1) == 4 and D(i+2) == 4 and D(i+3) == 4:
        print(i)
        quit()