# Точная степень двойки
n = int(input())
i = 0
x = "NO"
while 2**i <= n:
    if 2**i == n:
        x = "YES"
    i += 1
print(x)
