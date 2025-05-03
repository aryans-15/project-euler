def C(n):
    d, ub = 0, int(n**0.5) + 1
    for i in range(1, ub):
        if n % i == 0:
            if n / i == i:
                d += 1
            else:
                d += 2
    return d

i = 0

while C(i * (i + 1) // 2) < 500:
    i += 1

print(i * (i + 1) // 2)