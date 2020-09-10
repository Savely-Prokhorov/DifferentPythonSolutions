from math import sqrt


def cos(a, b, c):
    return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)


def cos_to_sin(cos):
    return sqrt(1 - cos ** 2)


sides = [3, 4, 4, 2]
diag = 5

cos1 = cos(sides[0], sides[1], diag)
sin1 = cos_to_sin(cos1)

cos2 = cos(sides[2], sides[3], diag)
sin2 = cos_to_sin(cos2)

s1 = 0.5 * sides[0] * sides[1] * sin1
s2 = 0.5 * sides[2] * sides[3] * sin2

print(round(s1 + s2, 2))
