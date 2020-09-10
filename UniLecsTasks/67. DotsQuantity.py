x1 = int(input("Type x1: "))
x2 = int(input("Type x2: "))
y1 = int(input("Type y1: "))
y2 = int(input("Type y2: "))

a = abs(x2 - x1)
b = abs(y2 - y1)

print(a)
print(b)

if a / b == a // b or b / a == b // a:
    if a >= b:
        print(b + 1)
    else:
        print(a + 1)
else:
    print(2)
