A = 0

for i in range(10, 354295):
    if i == sum(int(d)**5 for d in str(i)):
        A += i

print(A)