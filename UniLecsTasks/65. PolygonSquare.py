# using Gauss's area formula (Shoelace formula)
# https://en.wikipedia.org/wiki/Shoelace_formula

def square(x, y):
    sum1 = 0
    for i in range(len(x) - 1):
        sum1 += x[i] * y[i + 1]
    sum1 += x[i + 1] * y[0]

    sum2 = 0
    for i in range(len(x) - 1):
        sum2 -= x[i + 1] * y[i]
    sum2 -= x[0] * y[i + 1]

    return 0.5 * abs(sum1 + sum2)


x = [3, 5, 12, 9, 5]
y = [4, 11, 8, 5, 6]
print(square(x, y))
