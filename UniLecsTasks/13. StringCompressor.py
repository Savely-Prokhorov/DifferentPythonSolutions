"""
Задача: Написать функцию, ктр "сжимает" строку. Если полученная строка оказалась больше исходной, то вывести исходную.

Например, дана строка "ZZZABBEEE", получить строку вида "Z3A1B2E3", т.е. подставить счетчик вхождения символа.
"""

input_str = input("Enter string to compress: ")

output_str = ""
count = 1
prev = input_str[0]
for i in range(1, len(input_str)):
    letter = input_str[i]
    if letter == prev:
        count += 1
    else:
        output_str += prev + str(count)
        count = 1
    prev = letter

# adding last sequence
output_str += prev + str(count)

if len(output_str) > len(input_str):
    print(input_str)
else:
    print(output_str)
