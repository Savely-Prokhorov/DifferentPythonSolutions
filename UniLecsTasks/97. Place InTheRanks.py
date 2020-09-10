Arr = [155, 155, 154, 153, 150, 150, 147, 145, 144]
x = int(input("ВВедите рост Вани: "))

for i in range(0, len(Arr)-1):
    if Arr[i] >= x:
        if Arr[i+1] < x:
            res = i + 1 + 1
    # if Vanya is the tallest
    else:
        res = 1
    # if Vanya is the lowest
    if Arr[len(Arr) - 1] >= x:
        res = len(Arr) + 1

print(res)
