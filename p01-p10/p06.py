A, B = 0, 0
for i in range(1, 101):
    A += i
    B += i * i
print(A * A - B)