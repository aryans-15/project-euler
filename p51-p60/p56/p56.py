c = 0

for a in range(100):
    for b in range(100):
        c = max(c, sum(int(d) for d in str(pow(a, b))))

print(c)