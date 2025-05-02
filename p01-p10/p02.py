F, s = [0, 1], 0
while F[-1] <= 4e6:
    F.append(F[-1] + F[-2])
    if F[-1] % 2 == 0:
        s += F[-1]
print(s)