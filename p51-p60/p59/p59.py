import itertools, string

with open('../../files/p59.txt') as f:
    S = [int(x) for x in f.read().replace('"', '').split(",")]

keys = itertools.product(string.ascii_lowercase, repeat=3)

for kt in keys:
    k = ''.join(kt)
    dec = [c ^ [ord(ch) for ch in k][i % 3] for i, c in enumerate(S)]
    txt = ''.join(map(chr, dec))
    if all(word in txt for word in ["the", "be", "to", "of", "and", "a", "in", "that"]):
        print(sum(ord(c) for c in txt))
        quit()