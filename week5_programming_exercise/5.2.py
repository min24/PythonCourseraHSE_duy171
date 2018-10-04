# Ряд - 2
a = int(input())
b = int(input())
if a <= b:
    for i in range(a, b+1):
        print(i)
else:
    for i in list(range(b, a+1))[::-1]:
        print(i)
