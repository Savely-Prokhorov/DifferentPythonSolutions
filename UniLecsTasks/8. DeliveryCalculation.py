cost = int(input("Enter cost of purchase: "))
given = int(input("How much did you give? "))

delivery = given - cost

coins = [10, 5, 2, 1,
         0.5, 0.1, 0.01]
res = [0, 0, 0, 0,
       0, 0, 0]

print("Change: ", delivery)

change = delivery

for i, value in enumerate(coins):
    if value <= change:
        while value <= change:
            change -= value
            res[i] += 1

print("Chashier should return you: ")
for i in range(0, len(coins)):
    print(coins[i], ": ", res[i])
