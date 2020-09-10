def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

for n in range(2, 100001):
    if is_prime(n):
        print(n)
