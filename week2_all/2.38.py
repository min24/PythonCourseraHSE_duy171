# Второй максимум
n = int(input())
a = []
while n != 0:
    a += [n]
    n = int(input())
a = sorted(a)
print(a[-2])
