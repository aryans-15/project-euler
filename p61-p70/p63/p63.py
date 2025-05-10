c, n = 0, 1

while True:
    found = False
    for b in range(1, 10):
        if len(str(pow(b, n))) == n:
            c += 1
            found = True
    if not found:
        break
    n += 1

print(c)