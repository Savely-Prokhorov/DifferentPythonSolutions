def max_pofit(t, arr):
    arr.sort()
    arr.reverse()

    sum = 0
    for i in range(t):
        sum += arr[i]

    return sum


arr = [8, 2, 9, 17, 4, 4, 10]
t = 4

print(max_pofit(t, arr))
