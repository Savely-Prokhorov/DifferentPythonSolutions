n = int(input("n = "))

dividers = []
while n != 1:
    for i in range(2, n + 1):
        if i > n // 2 and i != n:
            pass
        else:
            if n % i == 0:
                n //= i
                dividers.append(i)

dividers.sort()
print(dividers)

count = 1
for i in range(0,  len(dividers) - 1):
    if dividers[i] == dividers[i + 1]:
        count += 1
    else:
        if count != 1:
            out = str(dividers[i]) + '^' + str(count)
            print(out, end='*')
        else:
            print(dividers[i], end='*')
        count = 1