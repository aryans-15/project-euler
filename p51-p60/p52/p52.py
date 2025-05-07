for i in range(1, 1000000):
    s = set()
    for j in range(1, 7):
        s.add(''.join(sorted(str(i*j))))
    if len(s) == 1:
        print(i)
        quit()