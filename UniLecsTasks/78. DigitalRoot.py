n = int(input("n = "))


def sum_digs(num):
    res = 0
    while num != 0:
        res += num % 10
        num //= 10
    return res

digital_root = n
while digital_root >= 10:
    digital_root = sum_digs(digital_root)

print(digital_root)
