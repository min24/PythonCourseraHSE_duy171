# Исполнитель раздвоитель
a = int(input())
b = int(input())
x = bin(a)
y = bin(b)
ans = []
while len(x) > len(y) and int(x, 2) >= int(y, 2):
    if x[-1] == '1':
        ans += ['-1'] + [':2']
        x = x[:-1]
    if x[-1] == '0':
        ans += [':2']
        x = x[:-1]
n = int(x, 2) - int(y, 2)
for i in range(n):
    ans += ['-1']
for i in ans:
    print(i)
