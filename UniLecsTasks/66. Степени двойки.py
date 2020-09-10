input_str = input("Введите строку: ")
input_len = len(input_str)

accum = ''
count = 0

while len(accum) < input_len:
    accum += str(2**count)
    count += 1

print(count)
