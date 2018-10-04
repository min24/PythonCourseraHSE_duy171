#  Количество палиндромов
n = int(input())
a = 0
i = 1
while i <= n:
    if str(i) == str(i)[::-1]:
        a += 1
    i += 1
print(a)
