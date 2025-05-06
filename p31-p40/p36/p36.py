c = 0

for i in range(1000000):
    # we have to remove the "0b" prefix from binary conversion, thus the [2:]
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
        c += i

print(c)