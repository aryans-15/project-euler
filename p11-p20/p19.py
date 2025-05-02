# 1 Jan 1901 was a Tuesday
S, E, d, c = 1901, 2000, 2, 0
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(S, E + 1):
    for j in range(12):
        if d == 0:
            c += 1
        if j == 1 and i % 4 == 0:
            d = (d + 1) % 7
        d = (d + days[j]) % 7
        
print(c)