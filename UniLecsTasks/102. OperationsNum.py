n = int(input("Enter number: "))

count = 0
while n != 1:
    if n % 3 == 0:
        n //= 3
    else:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
    count += 1

print(count)
