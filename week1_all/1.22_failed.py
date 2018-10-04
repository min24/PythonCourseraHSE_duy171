# Симметричное число *
n = 2015
x = str(n) == str(n)[::-1]
import random
y = random.randrange(0, 9999)
print(1*x + y*(1-x))

# Not working
