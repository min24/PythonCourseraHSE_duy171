# Среднее значение последовательности
n = int(input())
s = 0
c = 0
while n != 0:
    s += n
    c += 1
    n = int(input())
print(s/c)
