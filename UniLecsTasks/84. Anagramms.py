from functools import reduce


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)


def reduce_func(prev, cur):
    return prev * factorial(cur)


string = input("Введите слово: ")

sorted_str = sorted(list(string))

print(sorted_str)

el_dict = {}
count = 1
for i in range(0, len(sorted_str)-1):
    if sorted_str[i] == sorted_str[i+1]:
        count = count + 1
        el_dict[sorted_str[i]] = count
    else:
        count = 1
        el_dict[sorted_str[i+1]] = 1

print(el_dict)

denominators = [num for num in el_dict.values() if num >= 2]

print(denominators)

if denominators:
    denom = reduce(reduce_func, denominators)
else:
    denom = 1

res = factorial(len(string)) / denom

print(res)