# Uses python3

def fibonacci_sum_squares_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, cur = 0, 1
    summa = 1
    for i in range(2, n + 2):
        swap = cur % 10
        cur = (prev + cur) % 10
        prev = swap

    return (prev**2 + cur**2) % 10


n = int(input())
print(fibonacci_sum_squares_naive(n))
