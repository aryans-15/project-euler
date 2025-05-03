A = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = str(i * j)
        if prod == prod[::-1]:
            A = max(A, i*j)
print(A)