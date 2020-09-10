def exchange(a, b):
    a += b
    b = a - b
    a -= b
    return a, b

print(exchange(10, 30))
