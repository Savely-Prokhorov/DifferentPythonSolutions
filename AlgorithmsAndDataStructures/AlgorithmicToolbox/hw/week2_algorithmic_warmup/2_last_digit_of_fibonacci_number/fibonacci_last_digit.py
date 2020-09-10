# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    arr = [0 for i in range(n)]
    arr[0], arr[1] = 1, 1
    for i in range(2, n):
        arr[i] = (arr[i - 2] + arr[i - 1]) % 10

    return arr[-1]

#input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit_naive(n))
