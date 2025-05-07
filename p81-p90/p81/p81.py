with open('../../files/p81.txt') as f:
    S = [[int(x) for x in line.strip().split(",")] for line in f if line.strip()]

N = len(S)
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        dp[i][j] = S[i][j]
        if i > 0 and j > 0:
            dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        elif i > 0:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += dp[i][j-1]

print(dp[-1][-1])