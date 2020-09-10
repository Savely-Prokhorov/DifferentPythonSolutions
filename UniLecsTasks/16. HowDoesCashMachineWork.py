banknotes = [5000, 1000, 500, 100, 50]

cash = int(input("Введите сумму: "))


def choose_banknote(cash, out=[]):
    if cash > 0 and cash < 50:
        print("Невозможно выдать")
    else:
        if cash == 0:
            print(out)
        else:
            for banknote in banknotes:
                if cash >= banknote:
                    out.append(banknote)
                    cash -= banknote
                    choose_banknote(cash)
                    break


choose_banknote(cash)
