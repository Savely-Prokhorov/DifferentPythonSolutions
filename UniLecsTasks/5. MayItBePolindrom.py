"""
    Задача: Написать функцию, ктр будет проверять можно ли преобразовать строку так, чтобы она стала палиндромом.

    Пример:
    "bob" => true - уже является палиндромом
    "bbo" => true - можно сделать палиндромом
    "cat" => false - нельзя сделать палиндромом
"""
def count_letters(string):
    letters_dict = {}
    for letter in string:
        if letter not in letters_dict.keys():
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict


def has_less_than_one_odd(inclusions):
    count = 0
    for el in inclusions:
        if el % 2 == 1:
            count += 1
    if count < 2:
        return True
    else:
        return False

print(has_less_than_one_odd(count_letters('abcbccbba').values()))
