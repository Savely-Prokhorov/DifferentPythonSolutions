def nullify(start, end, arr):
    for i in range(start, end + 1):
        arr[i] = 0
    return arr


def count_parkings(scheme):
    for i in range(len(scheme)):
        if scheme[i] == 'S':
           nullify(i - 2, i, scheme)
        if scheme[i] == 'C':
           nullify(i - 1, i + 1, scheme)
        if scheme[i] == 'E':
           scheme[i] = 0

    count = 0
    for el in scheme:
        if el == '-':
            count += 1
    return count

scheme = "---S--C-E--C--"
scheme = list(scheme)

print(count_parkings(scheme))