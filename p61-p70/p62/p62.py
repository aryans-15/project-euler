a, n = {}, 1

while True:
    cube = pow(n, 3)
    key = ''.join(sorted(str(cube)))
    a[key] = a.get(key, []) + [cube]
    if len(a.get(key, [])) == 5:
        print(min(a[key]))
        quit()
    n += 1
