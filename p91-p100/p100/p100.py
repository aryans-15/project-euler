b, n = 15, 21

while n < pow(10, 12):
    b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3

print(b)