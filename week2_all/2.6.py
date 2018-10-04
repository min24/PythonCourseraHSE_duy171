# Квартиры
x = int(input())
y = int(input())
a = "NO"
if (x-1) % (y-x+1) == 0:
    a = "YES"
print(a)
