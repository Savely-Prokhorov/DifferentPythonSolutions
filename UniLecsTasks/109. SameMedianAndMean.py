def return_c(a, b):
    if (a + b) // 2 == (a + b) / 2:
        c = (a + b) // 2
    else:
        c = 2 * a - b
    return c

tests = [(1, 2), (1, 5), (1, 10), (100, 200)]

for test in tests:
    print(return_c(*test))
