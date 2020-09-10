arr = [1, 2, 4, 5]

sum1 = (arr[0] + arr[len(arr) - 1]) / 2 * (len(arr) + 1)
sum2 = sum(arr)

print(int(sum1 - sum2))
