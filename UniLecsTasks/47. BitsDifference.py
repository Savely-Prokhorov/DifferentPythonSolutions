n1 = 71
n2 = 15

n = n1 ^ n2  # применяем xor

count = 0
while n != 0:
    dig = n % 2
    if dig == 1:
        count += 1
    n //= 2

print(count)
