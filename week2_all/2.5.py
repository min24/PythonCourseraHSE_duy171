# Ход короля
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = 'NO'
if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
    a = 'YES'
print(a)
