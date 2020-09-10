def is_prime(num):
    divisors_count = 2
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors_count += 1
    if divisors_count == 2:
        return num

n = 2
user_input = ''
while user_input != 'exit':
    if is_prime(n):
        print(is_prime(n))
        user_input = input()
    n += 1
    if user_input == 'exit':
        break
