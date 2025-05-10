def P(n):
    if n < 2:
        return False
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

n = 2
while True:
    A = [i for i in range(2, n + 1) if P(i)]
    dp = [1] + [0] * n
    for p in A:
        for i in range(p, n + 1):
            dp[i] += dp[i - p]
    if dp[n] > 5000:
        print(n)
        quit()
    n += 1