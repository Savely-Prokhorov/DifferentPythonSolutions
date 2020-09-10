"""
Задача: дан числовой массив. Выполнить перестановку в массиве так,
 чтобы все четные элементы были слева, все нечетные - справа.
"""
def sort_arr(arr):
    count = 0
    for i in range(arr_len):
        if arr[i] % 2 == 0 and count != i:
            swap = arr[count]
            arr[count] = arr[i]
            arr[i] = swap
            count += 1
    return arr


arr = [i for i in range(100)]
arr_len = len(arr)

print(sort_arr(arr))
