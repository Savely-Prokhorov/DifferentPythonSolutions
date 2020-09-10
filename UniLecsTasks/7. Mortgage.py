apartement_price = int(input("Enter the price of your real estate: "))
years = int(input("Enter repayment period: "))
percent = int(input("Enter mortgage percent: ")) / 12 / 100
initial_payment = int(input("Enter your initial payment: "))

months = years * 12
precalculation = (1 + percent) ** months
coef = (percent * precalculation) / (precalculation - 1)
monthly_payment = (apartement_price - initial_payment) * coef

print()
print("Monthly payment: ", monthly_payment)
print("Overpayment: ", monthly_payment * months - apartement_price)


