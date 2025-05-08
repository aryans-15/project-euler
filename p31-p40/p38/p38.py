def P(n):
    return len(n) == 9 and set(n) == set("123456789")

a = 0

for i in range(10000):
    c, j = "", 1
    while len(c) < 9:
        c += str(i * j)
        j += 1
    if P(c):
        a = max(a, int(c))

print(a)