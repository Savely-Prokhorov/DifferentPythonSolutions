"""
    Дан массив целых чисел. Вывести все пары чисел в массиве, сумма ктр равна заданному целому числу X.
    Для примера используйте следующий массив:
    [ 3, 4, 5, -2, 10, 11, 12, -1, 0, 7, 8 ] 
    X = 10
"""

arr = [3, 4, 5, -2, 10, 11, 12, -1, 0, 7, 8]
summa = 10

iterations_num = len(arr) - 1
for i in range(iterations_num):
    for j in range(i + 1, iterations_num):
        if arr[i] + arr[j] == summa:
            print(arr[i], arr[j], sep=', ')
