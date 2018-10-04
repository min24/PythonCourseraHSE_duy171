# Ближайшее число
x = int(input())
y = str(input())
z = int(input())
t = list(map(int, y.split()))
a = list(map(lambda i: abs(i-z), t))
b = list(zip(a, t))
c = sorted(b, key=lambda i: i[0])
print(c[0][1])
