def D(n):
    return sum(int(d)**2 for d in str(n))

mp = {}

def C(n):
    s = [n]
    while n != 1 and n != 89:
        if n in mp:
            n = mp[n]
            break
        s.append(n)
        n = D(n)
    for num in s:
        mp[num] = n
    return n

count = 0
for i in range(1, 10000000):
    if C(i) == 89:
        count += 1

print(count)
