from sys import setrecursionlimit


def fibonacci(prev=1, cur=1):
    swap = cur
    cur += prev
    prev = swap
    print(cur)
    print()
    return fibonacci(prev, cur)

setrecursionlimit(2600)
fibonacci()
