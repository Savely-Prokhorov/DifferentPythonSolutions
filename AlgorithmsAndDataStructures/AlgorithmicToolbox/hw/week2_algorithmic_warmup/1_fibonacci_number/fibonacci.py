# Uses python3
def calc_fib(n):
    if n==0:
        return 0
    else:
        if n <= 2:
            return 1
    arr = [0 for i in range(n)]
    arr[0], arr[1] = 1, 1
    for i in range(2, n):
        arr[i] = arr[i-2] + arr[i-1]

    return arr[-1]

n = int(input())
print(calc_fib(n))
