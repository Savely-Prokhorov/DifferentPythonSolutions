n = int(input("Enter number: "))

cur, prev = 1, 1
while cur != n:
    cur += prev
    print(cur)
    prev = cur - prev
