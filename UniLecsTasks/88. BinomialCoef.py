def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

n = int(input("n = "))
k = int(input("k = "))

Cnk = factorial(n) / (factorial(k) * factorial(n - k))

print(Cnk)
