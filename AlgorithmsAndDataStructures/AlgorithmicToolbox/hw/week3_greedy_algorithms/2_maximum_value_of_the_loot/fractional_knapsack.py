# Uses python3
import sys

def find_max(n, weighted_cost):
    imax = 0
    for i in range(1, n):
        if weighted_cost[i]>weighted_cost[imax]:
            imax = i
    return imax;

def get_optimal_value(capacity, weights, values):
    value = 0.
    weighted_cost = [float(values[i])/float(weights[i]) for i in range(n)]
    # write your code here
    while capacity > 0:
        imax = find_max(n, weighted_cost)
        if weights[imax] <= capacity:
            value+=weighted_cost[imax]*weights[imax]
            weighted_cost[imax] = 0
            capacity -= weights[imax]
        else:
            value += weighted_cost[imax] * capacity
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
