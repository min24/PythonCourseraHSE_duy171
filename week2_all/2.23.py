# Спички *
l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
c = [(l1, r1, 1), (l2, r2, 2), (l3, r3, 3)]
a = sorted(c, key=lambda x: x[0])
x1 = a[1][0]-a[0][1]
x2 = a[2][0]-a[1][1]
x3 = a[2][0]-a[0][1]
m1 = a[0][1]-a[0][0]
m2 = a[1][1]-a[1][0]
m3 = a[2][1]-a[2][0]
x = []
if x3 <= 0 or (x1 <= 0 and x2 <= 0):
    x += [0]
if x1 > 0 and x2 <= 0:
    x += [a[0][2]]
if x2 > 0 and x2 <= m1:
    x += [a[0][2]]
if x2 > 0 and x2 <= -x1:
    x += [a[1][2]]
if x1 > 0 and x1 <= -x2:
    x += [a[1][2]]
if x1 <= 0 and x2 > 0:
    x += [a[2][2]]
if x1 > 0 and x1 <= m3:
    x += [a[2][2]]
if len(x) == 0:
    print(-1)
else:
    print(min(x))
