# Uses python3
import sys
import itertools

def partition3(n, A):
    T = [[[-1 for k in range(n)]for j in range(n)]for i in range(n)]
    for i in range(1,n):
        T[i][0][0] = A[i]
        T[0][i][0] = A[i]
        T[0][0][i] = A[i]
    print(T)
    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(n, A))

