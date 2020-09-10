def sum_elems(input_arr, ind_arr):
    res = 0
    for i in range(ind_arr[0] - 1, ind_arr[1]):
        res += input_arr[i]
    return res


arr = [i for i in range(1, 11)]
indexArr = [(1, 5), (2, 3), (3, 4)]

for array in indexArr:
    print(sum_elems(arr, array))
