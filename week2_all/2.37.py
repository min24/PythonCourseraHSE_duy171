# Количество элементов, больше предыдущего
n = int(input())
a = 0
while n != 0:
    b = n
    n = int(input())
    if b < n:
        a += 1
print(a)
