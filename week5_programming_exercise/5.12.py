# Переставить соседние
s = str(input())
x = list(map(int, s.split()))
x0 = x[::2]
x1 = x[1::2]
y = []
if len(x) % 2 == 0:
    for i, j in zip(x1, x0):
        y += [i] + [j]
else:
    for i, j in zip(x1, x0[:-1]):
        y += [i] + [j]
    y += [x0[-1]]
for i in y:
    print(i, end=' ')
