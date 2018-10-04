# Переставить min и max
s = str(input())
x = list(map(int, s.split()))
m = max(x)
n = min(x)
i = x.index(m)
j = x.index(n)
x[i] = n
x[j] = m
for i in x:
    print(i, end=' ')
