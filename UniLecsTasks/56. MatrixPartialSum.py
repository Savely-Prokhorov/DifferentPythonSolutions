def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(el, end=' ' * (4 - len(str(el))))  # хитрый способ настроить отступы для наилучшего вида
        print()


def partial_sum(matrix):
    psum = 0

    # будем заполнять эту матрицу
    # если сделаем копию, будем изменять исходную матрицу во время итераций
    # этого нам не надо, а с пустой не получится, Exception
    res_matrix = [[0 for row in range(len(matrix[0]))] for col in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for m in range(row + 1):
                for n in range(col + 1):
                    psum += matrix[m][n]
                    res_matrix[row][col] = psum
            psum = 0

    return res_matrix


matrix = [[1, 2, 3, 4, 5],
          [5, 4, 3, 2, 1],
          [2, 3, 1, 5, 4]]

print_matrix(matrix)

print()
print_matrix(partial_sum(matrix))
