import random

ccp, chp, g2j, jail, rr, uu = {2, 17, 33}, {7, 22, 36}, 30, 10, [5, 15, 25, 35], [12, 28]

cc_deck = ['GO', 'JAIL'] + ['NONE'] * 14
ch_deck = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'RR', 'RR', 'U', 'BACK3'] + ['NONE'] * 6
random.shuffle(cc_deck)
random.shuffle(ch_deck)

cp, hp, pos, cnt = 0, 0, 0, {}

for _ in range(500000):
    dc = 0
    while True:
        d1, d2 = random.randint(1, 4), random.randint(1, 4)
        dc = dc + 1 if d1 == d2 else 0
        if dc == 3:
            pos = jail
            break
        pos = (pos + d1 + d2) % 40
        if pos == g2j:
            pos = jail
            break
        if pos in ccp:
            c = cc_deck[cp]
            cp = (cp + 1) % 16
            if c == 'GO':
                pos = 0
            elif c == 'JAIL':
                pos = jail
        elif pos in chp:
            c = ch_deck[hp]
            hp = (hp + 1) % 16
            if c == 'GO':
                pos = 0
            elif c == 'JAIL':
                pos = jail
            elif c == 'C1':
                pos = 11
            elif c == 'E3':
                pos = 24
            elif c == 'H2':
                pos = 39
            elif c == 'R1':
                pos = 5
            elif c == 'RR':
                pos = next((r for r in rr if r > pos), rr[0])
            elif c == 'U':
                pos = next((u for u in uu if u > pos), uu[0])
            elif c == 'BACK3':
                pos = (pos - 3) % 40
                if pos == g2j:
                    pos = jail
                elif pos in ccp:
                    c2 = cc_deck[cp]
                    cp = (cp + 1) % 16
                    if c2 == 'GO':
                        pos = 0
                    elif c2 == 'JAIL':
                        pos = jail
        if d1 != d2:
            break
    cnt[pos] = cnt.get(pos, 0) + 1

s = sum(cnt.values())
P = {p: cnt[p] / s for p in cnt}
A = sorted(P, key=lambda p: (-P[p], p))[:3]
print(''.join(f"{p:02d}" for p in A))
