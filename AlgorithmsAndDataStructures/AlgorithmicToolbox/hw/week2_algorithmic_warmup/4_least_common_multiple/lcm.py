# Uses python3
import sys

def lcm_naive(a, b):
    save_a, save_b = a, b
    while a!=0 and b!=0:
        if a >= b:
            remainder = a % b
            a = remainder
        else:
            remainder = b % a
            b = remainder

    gcd = max(a,b)
    return gcd * save_a // gcd * save_b // gcd

a, b = map(int, input().split())
print(lcm_naive(a, b))
