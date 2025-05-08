ans, m = 0, 0

for p in range(1001):
    tmp = 0
    for a in range(1, p // 3):
        for b in range(a, 2 * p // 3):
            c = p - a - b
            if a * a + b * b == c * c:
                tmp += 1
    if tmp > m:
        m = tmp
        ans = p

print(ans)