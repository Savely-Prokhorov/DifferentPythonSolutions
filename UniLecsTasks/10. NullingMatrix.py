"""
    Задача: Если элемент матрицы равен 0, то всю строку и весь столбец нужно обнулить.
"""
from random import randint

matrix = [[randint(0, 10) for i in range(0, 5)] for i in range(0, 4)]

for inner_arr in matrix:
    for j in inner_arr:
        print(j, end=' ' * (5 - len(str(j))))  # хитрый способ настроить отступы для наилучшего вида
    print()

rows = []
columns = []
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] == 0:
            rows.append(i)
            columns.append(j)

for row in rows:
    for col in range(0, len(matrix[0])):
        matrix[row][col] = 0

for col in columns:
    for row in range(0, len(matrix)):
        matrix[row][col] = 0

print()
for inner_arr in matrix:
    for j in inner_arr:
        print(j, end=' ' * (5 - len(str(j))))  # хитрый способ настроить отступы для наилучшего вида
    print()
