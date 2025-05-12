import itertools
import operator

def E(ex):
    try:
        val = eval(ex)
        if abs(val - round(val)) < 1e-9:
            val = int(round(val))
        else:
            return None
        if val > 0:
            return val
    except ZeroDivisionError:
        return None

def F(s):
    i = 1
    while i in s:
        i += 1
    return i - 1

def G(n, s):
    a, b, c, d = n
    op1, op2, op3 = s
    A = []
    A.append(f'(({a}{op1}{b}){op2}{c}){op3}{d}')
    A.append(f'({a}{op1}({b}{op2}{c})){op3}{d}')
    A.append(f'({a}{op1}{b}){op2}({c}{op3}{d})')
    A.append(f'{a}{op1}(({b}{op2}{c}){op3}{d})')
    A.append(f'{a}{op1}({b}{op2}({c}{op3}{d}))')
    return A

ans, l, dig = None, 0, "0123456789"
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

for d in itertools.combinations(dig, 4):
    res = set()
    for nums in itertools.permutations(d):
        for syms in itertools.product(ops.keys(), repeat=3):
            for ex in G(nums, syms):
                val = E(ex)
                if val is not None:
                    res.add(val)
    run = F(res)
    if run > l:
        l, ans = run, d

print(''.join(ans))