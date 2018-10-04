# Шашки
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = x2-x1
y = y2-y1
a = "NO"
if 0 <= x <= y and ((y-x) % 2 == 0):
    a = "YES"

print(a)
