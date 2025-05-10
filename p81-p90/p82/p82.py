with open('../../files/p82.txt') as f:
    S = [[int(x) for x in line.strip().split(",")] for line in f if line.strip()]

N, dp = len(S), [r[0] for r in S]

for c in range(1, N):
    dp = [dp[r] + S[r][c] for r in range(N)]
    for r in range(1, N):
        dp[r] = min(dp[r], dp[r-1] + S[r][c])
    for r in range(N - 2, -1, -1):
        dp[r] = min(dp[r], dp[r+1] + S[r][c])

print(min(dp))