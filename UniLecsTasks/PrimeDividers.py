def is_prime(num):
    divisors_count = 2
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors_count += 1
    if divisors_count == 2:
        return True
    else:
        return False


n = int(input("Enter number: "))

divisor = 2
while n != 1:
    for divisor in range(2, n + 1):
        if n % divisor == 0 and is_prime(divisor):
            n //= divisor
            print(divisor)
