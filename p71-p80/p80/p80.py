import math
from decimal import Decimal, getcontext

getcontext().prec = 102

tot = 0
for i in range(1, 101):
    if pow(math.isqrt(i), 2) == i:
        continue
    tot += sum(int(d) for d in str(Decimal(i).sqrt()).replace('.', '')[:100])

print(tot)