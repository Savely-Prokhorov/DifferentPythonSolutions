"""
Найти элемент в отсортированной матрице 
(матрица, в ктр строки и столбцы отсортированы)
"""

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ' * (4 - len(str(el))))  # хитрый способ настроить отступы для наилучшего вида
        print()


def find_el(matrix, x):
    ind = [0, 0]
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(0, rows):
        if x in range(matrix[row][0], matrix[row][cols - 1] + 1):
            ind[0] = row
            for col in range(rows):
                if matrix[row][col] == x:
                    ind[1] = col
            break
    return ind

matrix = [[1, 5, 10, 20],
          [7, 9, 15, 28],
          [12, 25, 30, 36],
          [22, 35, 45, 50]]
x = 45

print_matrix(matrix)

print(find_el(matrix, x))
