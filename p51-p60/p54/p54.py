import treys

with open("../../files/p54.txt") as f:
    lines = [line.strip() for line in f]

E, w = treys.Evaluator(), 0

for line in lines:
    cards = line.strip().split()
    hand1 = [treys.Card.new(c[0] + c[1].lower()) for c in cards[:5]]
    hand2 = [treys.Card.new(c[0] + c[1].lower()) for c in cards[5:]]
    w += E.evaluate([], hand1) < E.evaluate([], hand2)

print(w)