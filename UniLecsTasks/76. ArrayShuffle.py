from itertools import zip_longest

arr = [1, 2, 3, 4]
shuffled_arr = [1, 4, 2, 3, 10, 15, 6, 17]

sorted_arr = sorted(arr)
sorted_shuffled_arr = sorted(shuffled_arr)

if sorted_arr == sorted_shuffled_arr:
    print(0)
else:
    zipped_arr = list(zip_longest(sorted_arr, sorted_shuffled_arr))
    print(zipped_arr)
    for tpl in zipped_arr:
        if tpl[0] != tpl[1]:
            print(tpl[1])
            break
