num = 12345678998765


def length(n, count):
    if n != 0:
        count += 1
        return length(n // 10, count)
    else:
        return count


def reverse(n, length, res):
    if n != 0:
        res += (n % 10) * 10 ** (length - 1)
        length -= 1
        return reverse(n // 10, length, res)
    else:
        return res


counter = 0
res = 0
print(reverse(num, length(num, counter), res))
