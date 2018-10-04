# Цвет клеток шахматной доски
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = (x1-x2) + (y1-y2)
b = 'NO'
if a % 2 == 0:
    b = 'YES'
print(b)
