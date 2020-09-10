arr = [0, 4, -1, 0, 4]

arr.sort()

for i in range(0, len(arr) - 1, 2):
    if arr[i] != arr[i + 1]:
        print(arr[i])
        break
