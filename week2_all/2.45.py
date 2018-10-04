# Максимальное число подряд идущих равных
n = int(input())
a = []
while n != 0:
    a += [n]
    n = int(input())
b = 0
c = 1
d = []
for i in range(1, len(a)):
    if a[i] == b:
        c += 1
    elif a[i] == a[i-1]:
        b = a[i]
        c += 1
    else:
        d += [c]
        c = 1
    d += [c]
print(max(d))
