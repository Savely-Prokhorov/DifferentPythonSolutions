"""
Какое минимальное количество спичек необходимо для того,
чтобы выложить на плоскости N квадратов со стороной в одну спичку?
 
Напишите программу, которая по количеству квадратов N, 
которое необходимо составить, находит минимальное необходимое для этого количество спичек.
"""
from math import ceil

def count_matches(squares):
    to_subtract = 0
    n = ceil(squares ** 0.5)

    rest = n ** 2 - squares

    # если в остатке больше строки
    if rest != 0:
        rows = rest // n + 1
        first_row_squares = rest - (rows - 1) * n
        to_subtract = first_row_squares * 2 + (rows - 1) * 3 + (rows - 1) * (n - 1) * 2

    res = (n - 1) * 2 * 3 + (n - 1) * (n - 1) * 2 + 4 - to_subtract
    return res

for n in range(1, 101):
    print(count_matches(n), end="; ")
