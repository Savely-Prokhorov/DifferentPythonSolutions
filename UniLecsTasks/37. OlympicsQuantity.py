from math import fsum

k = 0.25
m = 0.5
n = 0.2
d = 1

s = d / (1 - k - m - n)
print(1 - k - m - n)
print(fsum([-k, -m, -n]))

print(s)