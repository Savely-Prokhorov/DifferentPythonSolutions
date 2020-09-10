from random import random

n = int(input("Enter number of flips: "))


history = {'eagle': 0, 'tails': 0}
for i in range(0, n):
    rand_num = random()
    if round(rand_num) == 0:
        history['eagle'] += 1
    else:
        history['tails'] += 1

print(history)
