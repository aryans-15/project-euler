y, x, n, a = 14, 8, pow(10, 9), 0

while y <= n-2:
    a += y+2
    y, x = 7*y+12*x, 4*y+7*x

y, x = 52, 30

while y <= n+2:
    a += y-2
    y, x = 7*y+12*x, 4*y+7*x

print(a)