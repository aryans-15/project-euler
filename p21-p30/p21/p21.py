def S(n):
    a = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a += i
            if n // i != i:
                a += n // i
    return a

a = 0
for i in range(2, 10000):
    v = S(i)
    if v != i and S(v) == i:
        a += i

print(a)