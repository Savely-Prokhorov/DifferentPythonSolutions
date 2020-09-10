def subtract(x, y):
    return x + (-1) * y


def multiply(x, y):
    summa = 0
    for i in range(abs(y)):
        summa += abs(x)
    if x < 0 and y > 0 or y < 0 and x > 0:
        return summa * (-1)
    else:
        return summa


def divide(x, y):
    count = 0
    num = abs(x)
    while num != 0:
        num = subtract(abs(num), abs(y))
        count += 1

    if x < 0 and y > 0 or y < 0 and x > 0:
        return count * (-1)
    else:
        return count


x = 25
y = -5

print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))