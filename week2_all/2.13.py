# Тип треугольника
a = int(input())
b = int(input())
c = int(input())
x = a**2 + b**2 + c**2
y = a+b+c
z = max(a, b, c)
if 2*z >= y:
    print("impossible")
elif x == 2*z**2:
    print("rectangular")
elif x > 2*z**2:
    print("acute")
else:
    print("obtuse")
