# Сколько совпадает чисел
a, b, c = input(), input(), input()
x = len({a, b, c})
if x == 3:
    print(0)
else:
    print(4-x)
