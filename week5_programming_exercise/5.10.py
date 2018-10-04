# Наименьший положительный
s = str(input())
x = s.split()
x = map(int, x)
y = filter(lambda i: i > 0, x)
print(min(y))
