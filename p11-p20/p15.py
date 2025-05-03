import math
# Equivalent to "how many ways can we rearrange the string with 20 Rs and 20 Ds"
print(math.factorial(40) // pow(math.factorial(20), 2))