# Четные и нечетные
a = int(input())
b = int(input())
c = int(input())
x = (a % 2) + (b % 2) + (c % 2)
if x > 0 and x < 3:
    print("YES")
else:
    print("NO")
