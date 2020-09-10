# python3
import sys


def compute_min_refills(distance, tank, n, stops):
    # write your code here
    numRefills, curRefill = 0, 0
    while curRefill <= n:
        lastRefill = curRefill
        while (curRefill <= n and stops[curRefill+1] - stops[lastRefill] <= tank):
            curRefill+=1
        if curRefill == lastRefill:
            return -1
        if curRefill <= n:
            numRefills+=1
    return numRefills

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    stops.append(d)
    stops.append(0)
    for i in range(n, -1, -1):
        stops[i+1]=stops[i]
    stops[0] = 0

    print(compute_min_refills(d, m, n, stops))
