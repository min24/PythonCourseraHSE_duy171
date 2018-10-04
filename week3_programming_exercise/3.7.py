# Квадратное уравнение - 1
a = float(input())
b = float(input())
c = float(input())
dt = b**2 - 4*a*c
if dt < 0:
    print()
elif dt == 0:
    print(-b/(2*a))
else:
    x1 = (-b + dt**0.5)/(2*a)
    x2 = (-b - dt**0.5)/(2*a)
    print(min(x1, x2), max(x1, x2))
