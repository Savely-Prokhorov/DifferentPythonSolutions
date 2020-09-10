def add_digit(num, length, count=0):
    cur_len = len(num)
    if cur_len == length:
        count += 1
        return count
    else:
        if cur_len >= 2 and num[-2] == num[-1] and num[-1] == '1':
            return add_digit(num + '0', length, count)
        else:
            count = add_digit(num + '1', length, count)
            return add_digit(num + '0', length, count)


n = int(input("Введите длину последовательности: "))
print(add_digit('', n))
