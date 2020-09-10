"""
    Дана числовая матрица NxN. Напишите функцию, поворачивающую матрицу на 90 градусов
"""
from random import randint


def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ' * (4 - len(str(el))))  # хитрый способ настроить отступы для наилучшего вида
        print()


def rotate(matrix):
    matrix = list(zip(*matrix))
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(reversed(row)))
    return new_matrix


n = int(input('Введите размер квадратной матрицы: '))

matrix = [[randint(0, 10) for i in range(n)] for j in range(n)]
print_matrix(matrix)

rotated_matrix = rotate(matrix)

print()
print_matrix(rotated_matrix)
