# картинка с количеством точек пересечения и условиями:
# http://tepka.ru/geometriya/20.2.gif

def count_intesection(x1, y1, r1, x2, y2, r2):
    if y1 == y2:
        d = abs(x2 - x1)
    else:
        d = ((x2 - x1) ** 2 + y2 ** 2) ** 0.5

    r_sum = r1 + r2
    r_dif = abs(r1 - r2)

    if d > r_sum or d > 0 and d < r_dif:
        return 0
    if d == r_sum or d == r_dif:
        return 1
    if d > r_dif and d < r_sum:
        return 2
    return 'Infinity'

x1, y1, r1 = 0, 0, 5
x2, y2, r2 = 5, 0, 5

print(count_intesection(x1, y1, r1, x2, y2, r2))
