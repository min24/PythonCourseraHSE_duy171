# Количество четных элементов 
n = int(input())
a = 0
while n != 0:
    if n % 2 == 0:
        a += 1
    n = int(input())
print(a)
