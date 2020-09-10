arr = [i for i in range(1, 1001)]
print(arr)

res = []
for i in range(len(arr)):
    indexes = list(filter(lambda el: el != arr[i], arr))
    product = 1
    for el in indexes:
        product *= el
    res.append(product)

print(res)
