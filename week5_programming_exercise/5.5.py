# Четные индексы
s = str(input())
x = s.split(' ')[::2]
for i in x:
    print(i, end=' ')
