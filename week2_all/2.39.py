# Количество элементов, равных максимуму
n = int(input())
a = []
while n != 0:
    a += [n]
    n = int(input())
print(a.count(max(a)))
