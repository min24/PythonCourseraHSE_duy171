# Узник замка Иф
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x = sorted([a, b, c])
y = sorted([d, e])
if (x[0] <= y[0]) and (x[1] <= y[1]):
    print("YES")
else:
    print("NO")
