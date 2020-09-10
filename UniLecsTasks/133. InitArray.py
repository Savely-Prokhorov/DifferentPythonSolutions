n = int(input("Enter N: "))

# заполняем всю матрицу нулями
arr = [[0 for i in range(0, n)] for i in range(0, n)]

# заполняем пространство над побочной диагональю
for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        arr[i][j] = 1

# заполняем пространство под побочной диагональю
for i in range(1, n):
    for j in range(n - i, n):
        arr[i][j] = -1

# вывдом массив красиво
for inner_arr in arr:
    for j in inner_arr:
        print(j, end=' ' * (5 - len(str(j))))  # хитрый способ настроить отступы для наилучшего вида
    print()
