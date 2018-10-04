# Второе вхождение
s = str(input())
t = zip(list(s), range(len(s)))
x = filter(lambda i: i[0] == 'f', t)
x = list(x)
if len(x) == 0:
    print(-2)
elif len(x) == 1:
    print(-1)
else:
    print(x[1][1])
