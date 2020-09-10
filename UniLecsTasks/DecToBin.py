numeral_system = int(input("Введите основание системы счисления исходного числа: "))
num = int(input("Введите число: "))

res, count = 0, 0
digs_arr = []
if numeral_system == 2:
    while num != 0:
        dig = num % 2
        num //= 10
        res += dig * 2**count
        count += 1
    print(res)
else:
    while num != 0:
        dig = num % 2
        num //= 2
        digs_arr.append(str(dig))

digs_arr.reverse()
res = "".join(digs_arr)
print(res)
