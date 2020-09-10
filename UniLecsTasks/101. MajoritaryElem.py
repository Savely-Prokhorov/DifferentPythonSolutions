N = int(input("Размер массива: "))
print("Введите элементы массива: ")
arr = []
for i in range(0, N):
    arr.append(int(input()))

print(arr)
sorted_arr = sorted(arr)
print(sorted_arr)

el_dict = {}
count = 1
for i in range(0, N-1):
    if sorted_arr[i] == sorted_arr[i+1]:
        count = count + 1
        el_dict[sorted_arr[i]] = count
    else:
        count = 1
        el_dict[sorted_arr[i+1]] = 1

if N == 1:
    el_dict[sorted_arr[0]] = 1

arr_dict = list(el_dict.values())
res = max(arr_dict)
ind = arr_dict.index(res)
if res > int(float(N / 2)):
    print(list(el_dict.keys())[ind])
else:
    print("Такого нет")
