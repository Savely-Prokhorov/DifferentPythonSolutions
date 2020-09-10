"""
Задача: Дан отсортированный по возрастанию, но циклически сдвинутый массив. 
Нужно вывести индекс заданного элемента X (если такой элемент есть) в массиве.

Пример: [9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8]; X = 8

Вывод: 10
"""

def get_min_elem_ind(arr):
    for i in range(1, len(arr)):
        if arr[0] >= arr[i]:
            return i


def get_ind(min_el_ind, arr, el):
    for i in range(min_el_ind, len(arr)):
        if arr[i] == el:
            return i

arr = [9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8]
x = 5

print(get_ind(get_min_elem_ind(arr), arr, x))