str = '11_22_33_4_5_4_56_67'

symbols = {}

for symb in str:
    if symb not in symbols.keys():
        symbols[symb] = 1
    else:
        symbols[symb] += 1

for key in symbols.keys():
    if symbols[key] == 1:
        print(key)
        break
