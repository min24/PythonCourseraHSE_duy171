# Двоичный логарифм
n = int(input())
i = 0
while 2**i < n:
    i += 1
print(i)
