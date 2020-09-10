print("Введите коэффициенты a, b и с уравнения ax^2 + bx + c = 0")
a, b, c = map(int, input().split())
print("Вы ввели уравнение: ", end="")
if a != 0:
    print(a, "x^2", sep="", end="")
if b != 0:
    print(" {:+d}".format(b), "x ", sep="", end="")
if c != 0:
    print("{:+d}".format(c))

if a == 0:
    print("Уравнение является линейным")
    print("x = ", (-1)*c / b)
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = ((-1)*b + D**0.5) / (2*a)
        x2 = ((-1)*b - D**0.5) / (2*a)
        print("x1 = {}\nx2 = {}".format(x1, x2))
    else:
        if D == 0:
            x1 = (-1)*b / (2*a)
            print("Единственное действительное решение уравнения: x1 = ", x1)
        else:
            print("Данное квадратное уравнение не имеет решений на множестве действительных чисел")