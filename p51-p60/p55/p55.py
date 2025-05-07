c = 0

for i in range(10000):
    j, s = 0, str(i + int(str(i)[::-1]))
    while j < 50 and s != s[::-1]:
        s = str(int(s) + int(s[::-1]))
        j += 1
    if s != s[::-1]:
        c += 1

print(c)