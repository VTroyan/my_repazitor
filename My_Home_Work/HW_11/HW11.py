side1 = 4
side2 = 4
length = 15

geometric = [side1 * side2 ** (n - 1) for n in range(1, length + 1)]

print(geometric)
