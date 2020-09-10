# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    arr = [0, 1]
    k = 0
    for i in range(2, 6*m):
        arr.append((arr[i-1]+arr[i-2]) % m)
        k += 1
        if (arr[i] == 1) and (arr[i-1] == 0):
            break

    return arr[(n%k)]

n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
