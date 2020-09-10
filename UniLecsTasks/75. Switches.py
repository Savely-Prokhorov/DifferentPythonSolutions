# считаем кол-во простых делителей, прибавляем 1 и само число
# если полученное число четное, то выводим 0, иначе - 1
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def status(n):
    if n == 1:
        count = 1
    else:
        count = 2

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            count += 1

    if count % 2 == 0:
        return 0
    return 1

for n in range(1, 13):
    print(status(n))
