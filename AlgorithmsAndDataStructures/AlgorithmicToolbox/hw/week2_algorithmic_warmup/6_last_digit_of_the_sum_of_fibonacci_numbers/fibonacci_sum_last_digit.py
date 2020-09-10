# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n == 0:
        return 0
    prev, cur = 0, 1
    summa = 1
    for i in range(2, n+1):
        swap = cur
        cur = prev % 10 + cur % 10
        prev = swap
        summa = (summa + cur)%10

    return summa

n = int(input())
print(fibonacci_sum_naive(n))
