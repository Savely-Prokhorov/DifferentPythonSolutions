from math import pi

print('Введите два радиуса или длину хорды и ничего: ')
t = int(input())
r2 = input()

if r2 != '':
    r1 = t
    r2 = int(r2)
    del t
    radiuses_product = r1 * r2
else:
    radiuses_product = t ** 2 / 16

s = pi * 2 * radiuses_product

print(round(s, 2))
