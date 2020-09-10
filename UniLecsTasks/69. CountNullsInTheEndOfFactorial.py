def factorial(n):
    if n == 1:
        return 1
    else:
        if n == 2:
            return 2
        else:
            return n * factorial(n - 1)


def count_end_nulls(res):
    res = str(factorial(n))
    ind = len(res) - 1
    count = 0

    while res[ind] == '0':
        count += 1
        ind -= 1

    return count


n = int(input("Введите основание факториала: "))

print(count_end_nulls(str(factorial(n))))
