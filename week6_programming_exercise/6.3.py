# Создание архива
a = list(map(int, input().split()))
b = []
for i in range(a[1]):
    b += [int(input())]
b = sorted(b)
c = 0
k = 0
for i in b:
    d = c + i
    if d <= a[0]:
        c += i
        k += 1
print(k)
