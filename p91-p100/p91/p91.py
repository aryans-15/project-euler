c = 0

for x1 in range(51):
    for y1 in range(51):
        if x1 == 0 and y1 == 0: continue
        for x2 in range(51):
            for y2 in range(51):
                if x2 == 0 and y2 == 0: continue
                if x1 == x2 and y1 == y2: continue
                
                a2 = pow(x1, 2) + pow(y1, 2)
                b2 = pow(x2, 2) + pow(y2, 2)
                c2 = pow((x2 - x1), 2) + pow((y2 - y1), 2)
                
                c += a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2

print(c // 2)