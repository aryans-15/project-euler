def P(n):
    ub = int(n**0.5) + 1
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True

p, i = 3, 3

while p / (2 * i - 1) > 1/10:
    i += 2
    p += P(i*i) + P(i*i - i + 1) + P(i*i - 2*i + 2) + P(i*i - 3*i + 3)

print(i)