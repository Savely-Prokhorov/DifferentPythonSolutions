arr = [7, 7, 2, 7, 8, 7, 9, 7, 2, 2, 2]

arr.sort()

lines_num = {}
for el in arr:
    if el not in lines_num.keys():
        lines_num[el] = 1
    else:
        lines_num[el] += 1

print(lines_num)

count = 0
for el in lines_num.values():
    if el >= 4:
        count += 1

print(count)
