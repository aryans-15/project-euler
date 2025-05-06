C = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [1] + [0] * 200
for c in C:
    for j in range(c, C[-1] + 1):
        dp[j] += dp[j-c]
print(dp[-1])