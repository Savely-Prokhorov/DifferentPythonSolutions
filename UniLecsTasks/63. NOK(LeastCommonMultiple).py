def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            if a < b:
                b -= a
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def get_arr_lcm(arr):
    while len(arr) != 2:
        for i in range(0, len(arr) - 1, 2):
            arr[i] = lcm(arr[i], arr[i + 1])

        for i in range(1, len(arr) // 2 + 1):
            arr.pop(i)

    return lcm(arr[0], arr[1])


arr = [2, 12, 6, 24, 3]
print(get_arr_lcm(arr))
