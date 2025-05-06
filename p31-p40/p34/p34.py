import math
A = 0

for i in range(10, 2540161):
    if i == sum(math.factorial(int(d)) for d in str(i)):
        A += i

print(A)