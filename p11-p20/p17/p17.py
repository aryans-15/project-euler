import inflect

E, a = inflect.engine(), 0

for i in range(1, 1001):
    w = E.number_to_words(i).replace(" ", "").replace("-", "")
    a += len(w)

print(a)