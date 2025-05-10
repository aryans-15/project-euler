dp = [0] * 101
dp[0] = 1

for i in range(1, 101):
    for j in range(i, 101):
        dp[j] += dp[j - i]

print(dp[100] - 1)