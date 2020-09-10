# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    # while n >= 1:
    #     sequence.append(n)
    #     if n % 3 == 0:
    #         n = n // 3
    #     elif n % 2 == 0:
    #         n = n // 2
    #     else:
    #         n = n - 1
    a = [0 for i in range(n+1)]
    for i in range(2, n+1):
        if i % 2 == 0:
            if i % 3 == 0:
                a[i] = min(a[i-1], a[i//2], a[i//3]) + 1
            else:
                a[i] = min(a[i-1], a[i//2]) + 1
        else:
            if i % 3 == 0:
                a[i] = min(a[i - 1], a[i // 3]) + 1
            else:
                a[i] = a[i-1] + 1

    seq = []
    seq.append(n)
    i = n
    while i>0:
        if a[i-1] == a[i] - 1:
            seq.append(i-1)
            i -= 1
        else:
            if a[i//3] == a[i] - 1:
                seq.append(i//3)
                i //= 3
            else:
                seq.append(i//2)
                i //= 2

    return reversed(seq[:-1])

# input = sys.stdin.read()
n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
