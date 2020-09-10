from functools import reduce


def conc(str, cur):
    return str + cur

arr = [819, 6, 89, 47]

arr = [str(el) for el in arr]
arr.sort(reverse=True)

res = int(reduce(conc, arr, ""))

print(res)
