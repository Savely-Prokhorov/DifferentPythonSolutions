income = input("Enter income: ")
expenses = input("Enter expences: ")

income = sorted(income)

expenses = sorted(expenses)
expenses.reverse()

income = ''.join(income)
expenses = ''.join(expenses)

count = 0
if income[0] == '0':
    for i in range(0, len(income)):
        if income[i] == '0':
            count += 1
        else:
            break

    income = list(income)
    swap = ''.join(income[0: count])
    income = income[count:]
    income.insert(1, swap)
    income = ''.join(income)

print(expenses, " - ", income)
print(int(expenses) - int(income))
