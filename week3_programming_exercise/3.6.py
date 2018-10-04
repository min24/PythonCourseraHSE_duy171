# Проценты
p = float(input())
x = int(input())
y = int(input())
s = x*(1+p/100) + y*(1+p/100)/100 + 0.000001
k = str(s).split('.')
a = int(k[0])
if len(k[1]) == 1:
    b = int(k[1])*10
else:
    b = int(k[1][:2])
print(a, b)
