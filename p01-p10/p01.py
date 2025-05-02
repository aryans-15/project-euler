ans = 0
for i in range(1000):
    if i % 3 and i % 5:
        continue
    ans += i
print(ans)