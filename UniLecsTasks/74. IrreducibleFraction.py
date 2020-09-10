"""
Дробь x/n - называется правильной несократимой, если выполнены условия:
 1. 0 < X < N
 2. НОД(X, N) = 1

Входные данные: N - натуральное число, где N < 10^6.

Вывод: вывести кол-во правильных несократимых дробей со знаменателем N.

Пример:
1. N = 11, Result = 10
2. N = 12, Result = 4
3. N = 17, Result = 16
"""


# нахождение НОК
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            if a < b:
                b -= a
    return a

def count_irreducible_fractions(denom):
    numerator = 1
    count = 0

    while numerator < denom:
        if gcd(numerator, denom) == 1:
            count += 1
        numerator += 1

    return count

print(count_irreducible_fractions(11))
print(count_irreducible_fractions(12))
print(count_irreducible_fractions(17))
