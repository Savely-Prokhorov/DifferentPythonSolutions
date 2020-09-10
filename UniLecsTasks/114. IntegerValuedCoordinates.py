from math import floor

r = range(1, 101)

def count_points(r):
    total = 0
    for x in range(-r, 0):
        y = (r ** 2 - x ** 2) ** 0.5
        res = floor(y) * 2 + 1
        total += res

    total = total * 2 + (2 * r + 1)
    return total

for radius in r:
    print(count_points(radius))
