# Uses python3
import sys

def gcd_naive(a, b):
    while a!=0 and b!=0:
        if a >= b:
            remainder = a % b
            a = remainder
        else:
            remainder = b % a
            b = remainder

    return max(a,b)

a, b = map(int, input().split())
print(gcd_naive(a, b))
