n = int(input())
a = []
# Максимальная длина монотонного фрагмента
while n != 0:
    a += [n]
    n = int(input())
b = []
c = 1
if len(a) == 0:
    print(0)
elif len(a) == 1:
    print(1)
else:
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            c += 1
        else:
            c = 1
        b += [c]
    print(max(b))
