# Результаты олимпиады
n = int(input())
x = []
for i in range(n):
    x += [str(input()).split()]
y = []
for i in x:
    y += [(i[0], int(i[1]))]
y = sorted(y, key=lambda x: x[1])[::-1]
for i in y:
    print(i[0])
