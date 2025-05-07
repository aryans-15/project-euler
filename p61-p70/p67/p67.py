with open('../../files/p67.txt') as f:
    S = [[int(x) for x in line.strip().split()] for line in f if line.strip()]

N = len(S)
dp = [[0] * N for _ in range(N)]
dp[0][0] = S[0][0]

for i in range(1, N):
    for j in range(i+1):
        dp[i][j] = S[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))