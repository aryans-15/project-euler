with open('../../files/p89.txt') as f:
    S = [line.strip() for line in f]

n_to_v = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

v_to_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}

a = 0

for x in S:
    t, p = 0, 0
    for c in reversed(x):
        v = v_to_n[c]
        if v < p:
            t -= v
        else:
            t += v
            p = v
    mn, n = "", t
    for val, num in n_to_v:
        while n >= val:
            mn += num
            n -= val
    a += len(x) - len(mn)

print(a)