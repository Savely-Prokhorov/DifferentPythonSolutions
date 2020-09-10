def does_symbols_repeat(string):
    char_arr = []
    for letter in string:
        if letter not in char_arr:
            char_arr.append(letter)
        else:
            return True
    return False


user_input = input("Введите строку, чтобы выйти введите пустую: ")
while user_input != '':
    print(does_symbols_repeat(user_input))
    user_input = input("Введите строку, чтобы выйти введите пустую: ")
