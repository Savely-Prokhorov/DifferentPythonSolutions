def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def count1(n):
    count = 0
    if n == 1:
        return 1
    if is_prime(n):
        count = count1(n-1) + 1
    else:
        while n != 1:
            for i in range(2, n + 1):
                if is_prime(i):
                    if n % i == 0:
                        count += i
                        n //= i
                        break
    return count

for i in range(2, 100):
    print(i, ' | ', count1(i))


