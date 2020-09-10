n = int(input('Введите кол-во знаков числа: '))


def num_generator(num, signs, count):
    if len(num) == signs:
        count += 1
        return count

    if len(num) >= 2 and num[-2] == num[-1] and num[-1] == '4':
        return num_generator(num + '7', signs, count)

    if len(num) >= 2 and num[-2] == num[-1] and num[-1] == '7':
        return num_generator(num + '4', signs, count)

    count = num_generator(num + '4', signs, count)
    return num_generator(num + '7', signs, count)


counter = 0
print(num_generator('', n, 0))
