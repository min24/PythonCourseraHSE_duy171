# Коробки
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
m = sorted([a, b, c])
n = sorted([x, y, z])
if m == n:
    print("Boxes are equal")
elif m[0] >= n[0] and m[1] >= n[1] and m[2] >= n[2] and m != n:
    print("The first box is larger than the second one")
elif m[0] <= n[0] and m[1] <= n[1] and m[2] <= n[2] and m != n:
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
