"""
    Задача: Дан числовой массив. Проверить, есть ли такие два числа в массиве, 
    перемножив которые мы получим заданное число X.
"""


def check(arr, x):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] == x:
                return True
    return False


arr = [i for i in range(1, 6)]
x = 150

print(check(arr, x))
