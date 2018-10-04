# Список степеней двойки
n = int(input())
i = 0
while 2**i <= n:
    print(2**i, end=' ')
    i += 1
