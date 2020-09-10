# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [0 for i in range(m+1)]
    coins[0], coins[1] = 0, 1
    for m in range(2, m+1):
        if m>=3:
            coins[m] = min(coins[m-1]+1, coins[m-3]+1)
        if m>=4:
            coins[m] = min(coins[m-1]+1, coins[m-3]+1, coins[m-4]+1)
        else:
            coins[m] = 1
    return coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
