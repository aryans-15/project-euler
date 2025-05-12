from constraint import Problem, AllDifferentConstraint

with open('../../files/p96.txt') as f:
    S = [v.strip() for i, v in enumerate(f) if i % 10]
    S = [''.join(S[i:i+9]) for i in range(0, len(S), 9)]

def F(puzzle):
    p = Problem()
    p.addVariables([f"C{r}{c}" for r in range(9) for c in range(9)], range(1, 10))

    for idx, ch in enumerate(puzzle):
        if ch != '0':
            r, c = divmod(idx, 9)
            p.addConstraint(lambda var, val=int(ch): var == val, (f"C{r}{c}",))

    for r in range(9):
        p.addConstraint(AllDifferentConstraint(), [f"C{r}{c}" for c in range(9)])
        
    for c in range(9):
        p.addConstraint(AllDifferentConstraint(), [f"C{r}{c}" for r in range(9)])

    for br in range(3):
        for bc in range(3):
            block = [f"C{r}{c}" for r in range(br*3, br*3+3) for c in range(bc*3, bc*3+3)]
            p.addConstraint(AllDifferentConstraint(), block)

    sol = p.getSolution()
    return sol["C00"]*100 + sol["C01"]*10 + sol["C02"]

print(sum(F(p) for p in S))
