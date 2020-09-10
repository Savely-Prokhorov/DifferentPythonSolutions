# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    val = [[None] * (len(w) + 1) for _ in range(W + 1)]
    for u in range(W + 1):
        val[u][0] = 0
    print(val)
    for i in range(1, len(w) + 1):
        for u in range(W + 1):
            val[u][i] = val[u][i-1]
            if u >= w[i - 1]:
                val[u][i] = max(val[u][i], val[u - w[i-1]][i-1] + w[i-1])
    return val[W][len(w)]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    W = 10
    n = 3
    w = [1, 4, 8]
    print(optimal_weight(W, w))
