D, a, c = 1001, 1, 1

for i in range(1, D // 2 + 1):
    a += 4 * c + 10 * 2 * i
    c += 4 * 2 * i

print(a)