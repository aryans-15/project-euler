lim, n = 1000000, 1
p = [1]

while True:
    t, k = 0, 1
    while True:
        g1 = k * (3 * k - 1) // 2
        if g1 > n:
            break
        g2 = k * (3 * k + 1) // 2
        s = 1 if k % 2 else -1
        t += s * p[n - g1]
        if g2 <= n:
            t += s * p[n - g2]
        k += 1
    t %= lim
    p.append(t)
    if t == 0:
        print(n)
        quit()
    n += 1