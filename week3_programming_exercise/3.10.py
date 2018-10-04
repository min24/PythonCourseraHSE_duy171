# Первое и последнее вхождение
s = str(input())
if 'f' not in s:
    print()
else:
    x = s.find('f')
    y = s.rfind('f')
    if x == y:
        print(x)
    else:
        print(x, y)
