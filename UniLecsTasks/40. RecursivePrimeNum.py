def is_prime(n, divider):
    if divider > n // 2:
        return True
    else:
        if n % divider != 0:
            return is_prime(n, divider + 1)
        else:
            return False

for n in range(2, 1001):
    if is_prime(n, 2):
        print(n)
