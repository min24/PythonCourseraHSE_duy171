# Сложное уравнение *
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a**2 + b**2 == 0:
    print("INF")
elif a != 0 and not (c**2 + d**2 == 0 or a*d == b*c):
    print(int(-b/a))
else:
    print("NO")
