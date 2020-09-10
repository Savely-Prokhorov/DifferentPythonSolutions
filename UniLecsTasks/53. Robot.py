program = 'RRSRRLRR'

count = 0
max_right = 0
max_left = 999999
for command in program:
    if command == 'L':
        count -= 1
    else:
        if command == 'R':
            count += 1
        else:
            pass
    if count > max_right:
        max_right = count
    if count < max_left:
        max_left = count

res = max_right - max_left + 1
print(res)
