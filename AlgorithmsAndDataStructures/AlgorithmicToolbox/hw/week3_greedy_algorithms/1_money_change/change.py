# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]
    count = 0
    while m > 0:
        if m-coins[0] >= 0:
            m-=10
        elif m-coins[1] >= 0:
            m-=5
        else:
            m-=1
        count+=1
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
