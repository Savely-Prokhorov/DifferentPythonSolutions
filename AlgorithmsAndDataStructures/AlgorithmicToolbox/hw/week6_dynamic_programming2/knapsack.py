# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    val = [[0 for _ in range(W + 1)] for _ in range(len(w)+1)]
    print(val)
    for i in range(1, len(w) + 1):
        for u in range(W + 1):
            val[i][u] = val[i-1][u]
            # check that item weight <= weight of current knapsack
            if u >= w[i-1]:
                val[i][u] = max(val[i][u], val[i-1][u-w[i-1]]+w[i-1])
    print(val)
    return

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
