from fractions import Fraction

lim, C, k = 100, [2], 1
while len(C) < lim:
    C.extend([1, 2*k, 1])
    k += 1
    
C = C[:lim]

F = Fraction(C[-1], 1)
for a in reversed(C[:-1]):
    F = a + Fraction(1, F)

print(sum(int(d) for d in str(F.numerator)))