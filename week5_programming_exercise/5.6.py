# Четные элементы
s = str(input())
x = s.split(' ')
y = filter(lambda i: int(i) % 2 == 0, x)
for j in y:
    print(j, end=' ')
