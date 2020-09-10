cc_number = input("Enter credit card number: ")


def check_luhn(cc_num):
    res = 0
    for i, dig in enumerate([int(n) for n in list(cc_number)]):
        if i % 2 == 0:
            product = 2 * dig
            if product > 9:
                dig = product - 9
            else:
                dig = product
        res += dig

    return True if res % 10 == 0 else False

print(check_luhn(cc_number))
