arr = ["1", "4", "3", "4", "5"]

words = ["4", "4"]
words = ["4", "4"]

arr_len = len(arr)
for i in range(arr_len):
    if arr[i] == words[0]:
        arr[i] = 1
    else:
        if arr[i] == words[1]:
            arr[i] = 2
        else:
            arr[i] = 0

print(arr)

min_count = 999999999
for i in range(arr_len - 1):
    if arr[i] != 0:
        count = 1
        while arr[i + count] == 0:
            if arr[i + count] == arr[i]:
                arr[i] = 0
            else:
                count += 1
        if arr[i + 1] != arr[i] and arr[i + 1] != 0:
            min_count = 0
            break
        if count < min_count:
            min_count = count - 1
    else:
        continue

print(min_count)
