# Количество положительных
s = str(input())
x = s.split(' ')
y = filter(lambda i: int(i) > 0, x)
print(len(list(y)))
