input_arr = [1, 2, 3, 4, 5, 6]
length = len(input_arr)

output_arr = []

res = 1
for i in range(0, length):
    for j in range(0, length):
        if input_arr[i] != input_arr[j]:
            res *= input_arr[j]
    output_arr.append(res)
    res = 1

print(output_arr)
