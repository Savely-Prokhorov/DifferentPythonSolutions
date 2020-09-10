"""
Задача: Дана гистограмма, она представлена числовым массивом: 

[3, 6, 2, 4, 2, 3, 2, 10, 10, 4]

Нужно посчитать объем воды (1 блок в гистограмме), ктр наберется внутри нее.
"""
from matplotlib import pyplot as plt
arr = [3, 6, 2, 4, 2, 3, 2, 10, 10, 4, 5, 6, 4, 10]

plt.bar(range(len(arr)), arr)
plt.show()

water = 0
j = 0
for i in range(len(arr) - 1):
    if i < j:
        continue

    if arr[i + 1] < arr[i]:
        start = i
        j = start + 1
        while arr[i] > arr[j]:
            water += arr[i] - arr[j]
            j += 1
print(water)
