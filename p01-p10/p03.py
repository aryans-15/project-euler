N, i = 600851475143, 2
while i * i <= N:
    if N % i == 0:
        N //= i
    else:
        i += 1
print(N)