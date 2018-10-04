# Високосный год
n = int(input())
x = 'NO'
if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    x = 'YES'
print(x)
